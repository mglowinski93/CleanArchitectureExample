from .django_settings import *
from .auth_settings import *
from .app_settings import *

try:
    from .local_settings import *  # type: ignore
except ImportError:
    pass
