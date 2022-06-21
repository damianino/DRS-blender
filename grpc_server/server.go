package main

import (
	"fmt"
	types "grpc.server/Types"
	"grpc.server/utils"
	"net"

	"google.golang.org/grpc"

	"grpc.server/drs_protocol"
)

func main() {
	l, err := net.Listen("tcp4", ":4000")
	utils.Check(err, "Failed listening on port 4000")

	s := drs_protocol.Server{}

	grpcServer := grpc.NewServer()

	drs_protocol.RegisterJobsManagerServer(grpcServer, &s)
	go grpcServer.Serve(l)

	var first string
	for {
		fmt.Scanln(&first)
		switch first {
		case "nodes":
			s.Nodes.Print()
			break
		case "jobs":
			s.Jobs.Print()
			break
		case "test":
			node := &s.Nodes[0]
			fmt.Print(node.Job.Tasks[0])
			break
		case "reset":
			s.Nodes = types.Nodes{}
			s.Jobs = types.Jobs{}
		}
	}
}
