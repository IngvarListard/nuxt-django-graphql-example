<template>
  <v-layout row wrap justify-center>
    <v-flex xs8 class="pb-1">
      <!-- emit'ы теперь нам не нужны -->
      <new-todo-form />
    </v-flex>
    <v-flex v-for="todo of todoList" :key="todo.id" xs8 class="my-1">
      <todo-item :todo="todo" />
    </v-flex>
  </v-layout>
</template>

<script>
import NewTodoForm from '../components/NewTodoForm'
import TodoItem from '../components/TodoItem'
// импортируем свеженаписанные запросы
import { GET_TODO_LIST } from '../graphql'

export default {
  components: { TodoItem, NewTodoForm },
  data() {
    return {
      todoList: []
    }
  },
  apollo: {
    // получаем список todoList. При таком обхявлении запроса переменная todoList
    // должна записаться результатами запроса, однако запрос должен называться
    // аналогично
    todoList: { query: GET_TODO_LIST }
  }
}
</script>
