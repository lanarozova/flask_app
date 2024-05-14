import enum


class EnumBaseClass(enum.Enum):
    @classmethod
    def list(cls):
        return list(map(lambda r: r.value, cls))


class RolesNamesEnum(EnumBaseClass):
    user = "user"
    admin = "admin"


class MessageCategoriesEnum(EnumBaseClass):
    info = "info"
    error = "error"
    warning = "warning"
