from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[^\w\s])(?=.*[\d])[^\s]{5,20}$',
        [
            'password must have at least 1 lowercase letter',
            'password must have at least 1 uppercase letter',
            'password must have at least 1 number',
            'password must have at least 1 special symbol',
        ]
    )

    NAME = (
        r'^[a-zA-Z]{2,15}$',
        'only letters, length from 2 to 20 chars'
    )

    PHONE = (
        r'^\+380[9683]{2}[0-9]{7}$',
        'invalid phone number'
    )

    def __init__(self, pattern, message: str | list[str]):
        self.pattern = pattern
        self.message = message
