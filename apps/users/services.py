import os
from uuid import uuid1


def upload_photo(instance, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join('users', instance.profile.user.email, f'{uuid1()}.{ext}')
