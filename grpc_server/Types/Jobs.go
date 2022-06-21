package types

import (
	"fmt"
	"github.com/google/uuid"
)

type Job struct {
	CustomerNode *Node
	Uuid         uuid.UUID
	Tasks        Tasks
}

type Jobs []Job

func NewJob(n *Node) Job {
	var job Job

	job.CustomerNode = n

	job.Uuid = uuid.New()

	var tasks Tasks
	var i int32
	for i = 0; i < 100; i++ {
		tasks[i].FragmentIndex = i
		tasks[i].IsRendered = false
	}
	job.Tasks = tasks

	return job
}

func (jobs *Jobs) JobByNodeExists(id uint32) bool {
	for _, job := range *jobs {
		if job.CustomerNode.Id == id {
			return true
		}
	}
	return false
}

func (jobs Jobs) GetJobByUuid(uuid string) *Job {
	for i := 0; i < len(jobs); i++ {

		if jobs[i].Uuid.String() == uuid {
			return &jobs[i]
		}
	}
	return nil
}

func (jobs *Jobs) AssignTaskToNode(uuid string, node *Node) int32 {
	job := jobs.GetJobByUuid(uuid)

	for i := 0; i < 100; i++ {
		if job.Tasks[i].Worker == nil {
			job.Tasks[i].Worker = node
			node.Task = &job.Tasks[i]
			return job.Tasks[i].FragmentIndex
		}
	}

	return -1
}

func (jobs *Jobs) GetJob() *Job {
	if len(*jobs) > 0 {
		return &(*jobs)[0]
	}
	return nil
}

func (job Job) AllTasksDone() bool {
	for _, task := range job.Tasks {
		if !task.IsRendered {
			return false
		}
	}
	return true
}

func (jobs *Jobs) DeleteJob(uuid uuid.UUID) {
	for i := 0; i < len(*jobs); i++ {
		if (*jobs)[i].Uuid == uuid {
			(*jobs)[i] = (*jobs)[0]
			*jobs = (*jobs)[1:]
		}
	}
}

func (jobs *Jobs) Print() {
	fmt.Printf("%+v\n", *jobs)
}
