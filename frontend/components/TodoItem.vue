<template>
  <v-card>
    <v-card-title class="pb-1" style="overflow-wrap: break-word;">
      <b>{{ todo.title }}</b>
      <v-spacer />
      <!-- Изменено событие -->
      <v-btn
        @click="remove"
        flat
        small
        icon
        style="position: absolute; right: 0; top: 0"
      >
        <v-icon :disabled="$nuxt.isServer" small>close</v-icon>
      </v-btn>
    </v-card-title>
    <v-card-text class="py-1">
      <v-layout row justyfy-center align-center>
        <v-flex xs11 style="overflow-wrap: break-word;">
          {{ todo.text }}
        </v-flex>
        <v-flex xs1>
          <div style="text-align: right;">
            <!-- Добавлена обработка клика -->
            <v-checkbox
              :value="todo.done"
              @click.once="toggle"
              hide-details
              class="pa-0 ma-0"
              style="display: inline-block;"
              color="green lighten-1"
            />
          </div>
        </v-flex>
      </v-layout>
    </v-card-text>
    <v-card-actions>
      <span class="grey--text">
        Выполнить до <v-icon small>event</v-icon> {{ todo.dueDate }} | Создано
        <v-icon small>calendar_today</v-icon> {{ todo.createdDate }}
      </span>
      <v-spacer />
      <span class="grey--text">
        <!-- Изменен путь получения имени категории -->
        <v-icon small>category</v-icon>Категория: {{ todo.category.name }}
      </span>
    </v-card-actions>
  </v-card>
</template>

<script>
// импортируем свеженаписанные запросы
import { GET_TODO_LIST, REMOVE_TODO, TOGGLE_TODO } from '../graphql'

export default {
  name: 'TodoItem',
  props: {
    todo: {
      type: Object,
      default: () => ({})
    }
  },
  // с этого момента изменения по-серьезнее
  methods: {
    toggle() {
      // Для запроса который возвращает измененный элемент не обязательно
      // вручную прописывать функцию update. Apollo сам найдёт в каких
      // запросах "участвует" измененная запись, и разошлет всем подписчикам
      // измененный объект. В нашем случае это запрос в компоненте index.vue
      // на получение списка Todo
      this.$apollo.mutate({
        mutation: TOGGLE_TODO,
        variables: {
          todoId: this.todo.id
        }
      })
    },
    remove() {
      // функция update не видит контекста this
      const todoId = this.todo.id
      this.$apollo.mutate({
        mutation: REMOVE_TODO,
        variables: {
          todoId
        },
        update(store, { data: { removeTodo } }) {
          if (!removeTodo) return
          // В случае успешного удаления удаляем текущий элемент из кэша
          const data = store.readQuery({ query: GET_TODO_LIST })
          data.todoList = data.todoList.filter(todo => todo.id !== todoId)
          // Самоуничтожаемся!
          store.writeQuery({ query: GET_TODO_LIST, data })
        }
      })
    }
  }
}
</script>
