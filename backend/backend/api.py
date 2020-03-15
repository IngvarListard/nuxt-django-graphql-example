import json
import graphene
from django.middleware.csrf import CsrfViewMiddleware

from backend.todo_list.schema import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)


class CustomCsrfMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if getattr(request, 'csrf_processing_done', False):
            return None
        if getattr(callback, 'csrf_exempt', False):
            return None
        try:
            body = request.body.decode('utf-8')
            body = json.loads(body)
        # в любой непонятной ситуации передаём запрос оригинальному CsrfViewMiddleware
        except (TypeError, ValueError, UnicodeDecodeError):
            return super(CustomCsrfMiddleware, self).process_view(request, callback, callback_args, callback_kwargs)
        # проверка на list, т.к. клиент может отправлять "батченные" запросы
        # https://blog.apollographql.com/batching-client-graphql-queries-a685f5bcd41b
        if isinstance(body, list):
            for query in body:
                # если внутри есть хотя бы одна мутация, то отправляем запрос
                # к оригинальному CsrfViewMiddleware
                if 'mutation' in query:
                    break
            else:
                return self._accept(request)
        else:
            # принимаем любые query без проверки на csrf
            if 'query' in body and 'mutation' not in body:
                return self._accept(request)
        return super(CustomCsrfMiddleware, self).process_view(request, callback, callback_args, callback_kwargs)
