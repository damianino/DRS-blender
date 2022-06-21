package drs_protocol

import (
	"fmt"
	"golang.org/x/net/context"
	"google.golang.org/grpc/peer"
	"grpc.server/Types"
	"grpc.server/utils"
	"strconv"
)

type Server struct {
	Nodes types.Nodes
	Jobs  types.Jobs
}

func (s *Server) ConnectRequest(ctx context.Context, request *Request) (*Response, error) {
	//	TODO: CHECK connection validity

	nodePtr := s.Nodes.GetNodePtrById(request.GetUserId()) // проверка повторного подключения
	if nodePtr != nil {
		return &Response{Success: true, Body: nodePtr.SessionKey}, nil
	}

	authKey := utils.RandSeq(10)
	p, _ := peer.FromContext(ctx)
	newNode := types.Node{request.GetUserId(), p.Addr.String(), authKey, types.Inactive, nil, nil}
	s.Nodes = append(s.Nodes, newNode)

	return &Response{Success: true, Body: authKey}, nil
}

func (s *Server) RenderRequest(ctx context.Context, request *Request) (*Response, error) {
	if !s.auth(request.GetUserId(), request.GetSessionKey()) {
		return &Response{Success: false, Body: "Authentication failed"}, nil
	}
	if s.Jobs.JobByNodeExists(request.GetUserId()) {
		return &Response{Success: false, Body: "Node already submitted a job"}, nil
	}

	// TODO
	nodePtr := s.Nodes.GetNodePtrById(request.GetUserId())
	newJob := types.NewJob(nodePtr)

	s.Jobs = append(s.Jobs, newJob)
	return &Response{Success: true, Body: newJob.Uuid.String()}, nil
}

func (s *Server) JobPollRequest(ctx context.Context, request *Request) (*JobPollResponseMessage, error) {

	if !s.auth(request.GetUserId(), request.GetSessionKey()) {
		return &JobPollResponseMessage{Success: false, Body: "Authentication failed", FragmentIndexes: -1}, nil
	}

	if len(s.Jobs) == 0 {
		return &JobPollResponseMessage{Success: false, Body: "No jobs available", FragmentIndexes: -1}, nil
	}

	node := s.Nodes.GetNodePtrById(request.GetUserId())

	if request.Body == "" {
		job := s.Jobs.GetJob()
		node.Job = job
		return &JobPollResponseMessage{Success: true, Body: job.CustomerNode.Ip + "|" + job.Uuid.String(), FragmentIndexes: -1}, nil
	}

	job := s.Jobs.GetJobByUuid(request.GetBody())
	if job != nil {
		fragmentIndex := s.Jobs.AssignTaskToNode(request.GetBody(), node)
		return &JobPollResponseMessage{Success: true, Body: job.CustomerNode.Ip, FragmentIndexes: fragmentIndex}, nil
	}

	return &JobPollResponseMessage{Success: true, Body: node.Ip, FragmentIndexes: 0}, nil
}

func (s *Server) UpdateRoleRequest(ctx context.Context, request *Request) (*Response, error) {
	if !s.auth(request.GetUserId(), request.GetSessionKey()) {
		return &Response{Success: false, Body: "bla bla"}, nil
	}
	node := s.Nodes.GetNodePtrById(request.GetUserId())
	node.Role, _ = strconv.ParseInt(request.Body, 10, 32)
	return &Response{Success: true, Body: "bla bla"}, nil
}

func (s *Server) ReportProgressRequest(ctx context.Context, request *Request) (*Response, error) {
	if !s.auth(request.GetUserId(), request.GetSessionKey()) {
		return &Response{Success: false, Body: "bla bla"}, nil
	}
	node := s.Nodes.GetNodePtrById(request.GetUserId())
	if node.Task == nil {
		return &Response{Success: false, Body: "No task was registered to this node"}, nil
	}
	fragmentIndex, err := strconv.ParseInt(request.GetBody(), 10, 32)
	if fragmentIndex < 0 || fragmentIndex > 99 || err != nil {
		return &Response{Success: false, Body: "Not a valid fragment index"}, nil
	}

	node.Job.Tasks[fragmentIndex].IsRendered = true
	node.Task = nil

	fmt.Printf("task %d rendered", fragmentIndex)

	if node.Job.AllTasksDone() {
		fmt.Printf("Job %s complete\n", node.Job.Uuid.String())
		s.Jobs.DeleteJob(node.Job.Uuid)
	}

	return &Response{Success: true, Body: "Task marked as rendered"}, nil
}

func (s *Server) auth(userId uint32, sessionKey string) bool {
	node := s.Nodes.GetNodePtrById(userId)
	if node != nil && node.SessionKey == sessionKey {
		return true
	}
	return false
}

func (s *Server) mustEmbedUnimplementedJobsManagerServer() {
}
