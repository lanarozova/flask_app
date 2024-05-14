from typing import NamedTuple


class NewUserDTO(NamedTuple):
    email: str
    name: str
    password: str
    is_active: bool
    role_id: int


class UserEntityDTO(NamedTuple):
    id: int
    name: str
    email: str
    is_active: bool
    role_id: int
