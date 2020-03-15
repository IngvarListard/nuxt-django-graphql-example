import gql from 'graphql-tag'

// т.к. внутренности записи Todo используются практически во всех запросах,
// то резонно вынести их в отдельный фрагмент
// https://www.apollographql.com/docs/react/data/fragments/
const TODO_FRAGMENT = gql`
  fragment TodoContents on TodoNode {
    id
    title
    text
    done
    createdDate
    dueDate
    category {
      id
      name
    }
  }
`

const ADD_TODO = gql`
  mutation(
    $title: String!
    $text: String
    $dueDate: Date!
    $category: String!
  ) {
    addTodo(
      title: $title
      text: $text
      dueDate: $dueDate
      category: $category
    ) {
      ...TodoContents
    }
  }
  ${TODO_FRAGMENT}
`

const TOGGLE_TODO = gql`
  mutation($todoId: ID) {
    toggleTodo(todoId: $todoId) {
      ...TodoContents
    }
  }
  ${TODO_FRAGMENT}
`

const GET_CATEGORIES = gql`
  {
    categories {
      id
      name
    }
  }
`

const GET_TODO_LIST = gql`
  {
    todoList {
      ...TodoContents
    }
  }
  ${TODO_FRAGMENT}
`

const REMOVE_TODO = gql`
  mutation($todoId: ID) {
    removeTodo(todoId: $todoId)
  }
`

export { ADD_TODO, TOGGLE_TODO, GET_CATEGORIES, GET_TODO_LIST, REMOVE_TODO }
