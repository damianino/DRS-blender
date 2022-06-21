package types

import (
	"errors"
	"fmt"
)

type Node struct {
	Id         uint32
	Ip         string
	SessionKey string
	Role       int64
	Job        *Job
	Task       *Task
}

type Nodes []Node

func (nodes Nodes) GetNodePtrById(id uint32) *Node {
	for i := 0; i < len(nodes); i++ {
		if nodes[i].Id == id {
			return &nodes[i]
		}
	}
	return nil
}

func (nodes Nodes) GetIndex(id uint32) (int, error) {
	for i, node := range nodes {
		if node.Id == id {
			return i, nil
		}
	}
	return -1, errors.New("node with given ID not found")
}

func (nodes Nodes) RemoveNodeById(id uint32) Nodes {
	i, err := nodes.GetIndex(id)
	if err != nil{
		return nodes
	}
	nodes[i] = nodes[len(nodes)-1]
	return nodes[:len(nodes)-1]
}

func (node Node) Print() {
	fmt.Printf("%+v\n", node)
}

func (nodes Nodes) Print() {
	fmt.Printf("%+v\n", nodes)
}
