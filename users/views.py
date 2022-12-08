from services import ReadWriteUserService, UserByIdService

from rest_framework.response import Response
from rest_framework.views import APIView

# Реалізовуємо ось такі EndPoints:
#
# GET http://localhost:8000/users           //витягнути всіх юзерів з файлу
# POST http://localhost:8000/users        // записати нового юзера в файл (не забудьте про id, він має бути унікальним)
#
# GET http://localhost:8000/users/<ID>           // витягти юзера по ID
# PUT http://localhost:8000/users/<ID>          // змінити юзера по ID
# DELETE  http://localhost:8000/users/<ID>          // видалити юзера по ID
#
# список юзерів зберігаємо в файлі users.json


class UsersView(APIView):
    def get(self, *args, **kwargs):
        users = ReadWriteUserService.load_users()
        return Response(users)

    def post(self, *args, **kwargs):
        users = ReadWriteUserService.load_users()
        user = self.request.data
        user['id'] = users[-1]['id'] + 1 if len(users) else 1
        users.append(user)
        res = ReadWriteUserService.write_user(users)
        print(res)
        return Response(res)


class UserByIdView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        return Response(UserByIdService.read_user(pk))

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = self.request.data
        user['id'] = pk
        return Response(UserByIdService.update_user(user))

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        return Response(UserByIdService.delete_user(pk))
