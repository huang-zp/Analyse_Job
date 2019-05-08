# 基础异常定义
class BaseError(Exception):
    def __init__(self, message='', code=400, **kwargs):
        self.code = code
        self.desc = message if message else '参数错误'


# 参数异常
class ParamError(BaseError):
    pass


# 业务异常
class BizError(BaseError):
    pass


# int类型异常
class IntegrityError(BaseError):
    pass

# 数据库异常
class DBError(BaseError):
    pass

# 角色全县异常
class AuthError(BaseError):
    pass


# 服务异常
class ServiceError(BaseError):
    """
    third party service error
    """
    pass


class PrivilegeError(BizError):
    pass


class ResourceNotFound(BizError):
    pass
