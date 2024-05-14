from abc import ABC, abstractmethod
from typing import Optional

from apps.main.data_objects.dto.user import UserEntityDTO, NewUserDTO
from apps.main.data_objects.dto.role import RoleEntityDTO
from apps.enums import RolesNamesEnum


class UserRepositoryInterface(ABC):

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserEntityDTO]:
        pass

    @abstractmethod
    def add_user(self, new_user: NewUserDTO) -> UserEntityDTO:
        pass


class RoleRepositoryInterface(ABC):

    @abstractmethod
    def get_user_role(self) -> Optional[RoleEntityDTO]:
        pass

    @abstractmethod
    def get_admin_role(self) -> Optional[RoleEntityDTO]:
        pass

    @abstractmethod
    def get_role(self, role_name: RolesNamesEnum) -> Optional[RoleEntityDTO]:
        pass
