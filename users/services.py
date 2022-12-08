import json


class ReadWriteUserService:
    file_name = 'users.json'

    @classmethod
    def load_users(cls):
        try:
            with open(cls.file_name) as file:
                return json.load(file)
        except Exception as err:
            print(f'{err=}')
            return []

    @classmethod
    def write_user(cls, users: list):
        try:
            with open(cls.file_name, 'w+') as file:
                json.dump(users, file)
                return users[-1]
        except Exception as err:
            print(err)
            return 'Can\'t write user'


class UserByIdService:
    file_name = ReadWriteUserService.file_name

    @classmethod
    def read_user(cls, pk: int):
        users = ReadWriteUserService.load_users()
        if len(users):
            res_user = 'Have no user with this id'
            for user in users:
                res_user = user if user['id'] == pk else res_user
            return res_user

    @classmethod
    def update_user(cls, user: dict):
        users = ReadWriteUserService.load_users()
        can_update = False
        for i, item in enumerate(users):
            if item['id'] == user['id']:
                users[i] = user
                can_update = True
                print(users)
        if can_update:
            try:
                with open(cls.file_name, 'w') as file:
                    json.dump(users, file)
                    return user
            except Exception as err:
                print(err)
                return 'Can\'t update user'
        else:
            return 'Can\'t update non-existent user'

    @classmethod
    def delete_user(cls, pk: int):
        user = cls.read_user(pk)
        users = ReadWriteUserService.load_users()
        if type(user) == dict:
            try:
                with open(cls.file_name, 'w') as file:
                    users.remove(user)
                    print(users)
                    json.dump(users, file)
                    return 'deleted successfully'
            except Exception as err:
                print(err)
                return 'Smth went wrong'
        else:
            return 'User not found'
