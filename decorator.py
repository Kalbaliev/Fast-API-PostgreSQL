import  random
import string
from functools import wraps


def api_key_creator(seed):
    random.seed(seed)
    api_key=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=24))
    return api_key


def check_api_key(func):

    @wraps(func)
    def wrapper(request,*args, **kwargs):

        if request.api_key == "qQQ0lojnTiGnsAZLarj2YXZU6Xp0EUIAwAthYX9QIUiPBkmGpCLyiEoomweO7yS5":
            return func(request,*args, **kwargs)
        else:
            return 'API-KEY is incorrect'
    return wrapper


