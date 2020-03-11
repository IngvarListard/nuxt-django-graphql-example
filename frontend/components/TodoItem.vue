<template>
  <v-card>
    <v-card-title class="pb-1" style="overflow-wrap: break-word;">
      <b>{{ todo.title }}</b>
      <v-spacer />
      <v-btn
        @click="$emit('delete', todo.id)"
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
          {{ todo.description }}
        </v-flex>
        <v-flex xs1>
          <div style="text-align: right;">
            <v-checkbox
              v-model="todo.done"
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
        <v-icon small>category</v-icon>Категория: {{ todo.category }}
      </span>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    todo: {
      type: Object,
      default: () => ({})
    }
  }
}
</script>
