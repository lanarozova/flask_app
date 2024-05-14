from typing import Optional

from sqlalchemy.exc import SQLAlchemyError

from apps.main.data_objects.dto.role import RoleEntityDTO
from apps.main.interfaces import UserRepositoryInterface, RoleRepositoryInterface
from apps.main.model import UserModel, Role
from apps.mixins import DBMixin
from apps.main.data_objects.dto.user import UserEntityDTO, NewUserDTO
from apps.enums import RolesNamesEnum
from apps.main.exceptions import UserNotFoundError, UserAlreadyRegisteredError


class UserRepository(UserRepositoryInterface, DBMixin):
    @staticmethod
    def _map_user_entity_dto(user: UserModel) -> UserEntityDTO:
        user_entity_dto = UserEntityDTO(
            name=user.name,
            id=user.id,
            email=user.email,
            is_active=user.is_active,
            role_id=user.role_id
        )
        return user_entity_dto

    def _commit_session(self, user: UserModel) -> None:
        db = self._get_db()

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def get_user_by_email(self, email: str):
        user = UserModel.query.filter(UserModel.email == email).first()
        if not user:
            return None
        return self._map_user_entity_dto(user)

    def check_user_password(self, email, password):
        user = UserModel.query.filter(UserModel.email == email).first()
        if not user.check_password(password):
            raise UserNotFoundError("Email or password is incorrect. "
                                    "Try resetting your password or register an account")
        return True

    def add_user(self, new_user: NewUserDTO):

        user_found = self.get_user_by_email(new_user.email)
        if user_found:
            raise UserAlreadyRegisteredError("User with such email already exists.")
        user = UserModel(
            name=new_user.name,
            email=new_user.email,
            role_id=new_user.role_id,
            password=new_user.password,
            is_active=True
        )
        self._commit_session(user)
        return self._map_user_entity_dto(user)


class RoleRepository(RoleRepositoryInterface, DBMixin):

    @staticmethod
    def _map_role_entity_dto(role: Role) -> RoleEntityDTO:
        role_entity_dto = RoleEntityDTO(
            id=role.id,
            name=role.name
        )
        return role_entity_dto

    def _commit_session(self, role: Role) -> None:
        db = self._get_db()
        try:
            db.session.add(role)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def get_user_role(self) -> Optional[RoleEntityDTO]:
        return self.get_role(RolesNamesEnum.user)

    def get_admin_role(self) -> Optional[RoleEntityDTO]:
        return self.get_role(RolesNamesEnum.admin)

    def get_role(self, role_name: RolesNamesEnum) -> Optional[RoleEntityDTO]:
        role = Role.query.filter(Role.name == role_name.value).first()
        if not role:
            role = Role(name=role_name.value)
            try:
                self._commit_session(role)
            except SQLAlchemyError:
                return None
        return self._map_role_entity_dto(role)
