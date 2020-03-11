<template>
  <v-layout row wrap justify-center>
    <v-flex xs8 class="pb-1">
      <new-todo-form @add="addTodo" />
    </v-flex>
    <v-flex v-for="todo of todoList" :key="todo.id" xs8 class="my-1">
      <todo-item :todo="todo" @delete="deleteTodo" />
    </v-flex>
  </v-layout>
</template>

<script>
import NewTodoForm from '../components/NewTodoForm'
import TodoItem from '../components/TodoItem'
export default {
  components: { TodoItem, NewTodoForm },
  data() {
    return {
      todoList: [
        {
          id: 1,
          title: 'TODO 1',
          description:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
          dueDate: '2020-10-16',
          createdDate: '2020-03-09',
          done: false,
          category: 'Работа'
        },
        {
          id: 2,
          title: 'TODO 2',
          description:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
          dueDate: '2020-10-16',
          createdDate: '2020-03-09',
          done: false,
          category: 'Работа'
        },
        {
          id: 3,
          title: 'TODO 3',
          description:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
          dueDate: '2020-10-16',
          createdDate: '2020-03-09',
          done: false,
          category: 'Работа'
        },
        {
          id: 4,
          title: 'TODO 4',
          description:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
          dueDate: '2020-10-16',
          createdDate: '2020-03-09',
          done: false,
          category: 'Работа'
        },
        {
          id: 5,
          title: 'TODO 5',
          description:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
          dueDate: '2020-10-16',
          createdDate: '2020-03-09',
          done: false,
          category: 'Работа'
        },
        {
          id: 6,
          title: 'TODO 6',
          description:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
          dueDate: '2020-10-16',
          createdDate: '2020-03-09',
          done: false,
          category: 'Работа'
        }
      ]
    }
  },
  methods: {
    addTodo(newTodo) {
      const id = this.todoList.length
        ? Math.max.apply(
            null,
            this.todoList.map(item => item.id)
          ) + 1
        : 1
      this.todoList.unshift({
        id,
        createdDate: new Date().toISOString().substr(0, 10),
        done: false,
        ...newTodo
      })
    },
    deleteTodo(todoId) {
      this.todoList = this.todoList.filter(item => item.id !== todoId)
    }
  }
}
</script>
