# nuxt-django-graphql-example
Пример построения dev окружения на стеке Nuxt + Django + GraphQL   
Репозиторий соответствующей [статьи на Хабре](https://habr.com/ru/post/492486/)

## Установка

```bash
pipenv install
pipenv run python manage.py migrate
npm install
```
## Запуск
Django dev server
```bash
pipenv run manage.py runserver
```

Npm dev server
```bash
npm run dev
```

После запуска приложение будет доступно на <http://localhost:3000>
