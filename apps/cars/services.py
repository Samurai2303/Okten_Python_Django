import os
from uuid import uuid1


def upload_car_photo(instance, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join('cars', instance.car.model, f'{uuid1()}.{ext}')
