import os
from uuid import uuid1


def upload_car_photo(instance, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join(instance.car.model, 'photos', f'{uuid1()}.{ext}')
