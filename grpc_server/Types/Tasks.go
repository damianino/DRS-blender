package types

import "fmt"

const ()

type Task struct {
	FragmentIndex int32
	Worker        *Node
	IsRendered    bool
}

type Tasks [100]Task

func (tasks *Tasks) AssignTasksTo(node *Node) {

}

func (task Task) Print() {
	fmt.Printf("%+v\n", task)
}

func (tasks Tasks) Print() {
	fmt.Printf("%+v\n", tasks)
}
