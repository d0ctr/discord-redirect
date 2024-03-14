from functools import wraps

unaccepted_chars = [
    '{', '}', '%', '"', '\'', '\\', '[', ']', '$'
]

def check_link_arg(index=0, name=None):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if len(args) == 0 and len(kwargs) == 0:
                return 'Bad Request', 403
            if name is None:
                line = args[index]
            else:
                line = kwargs[name]
            if line is not None:
                for char in unaccepted_chars:
                    if char in line:
                        return 'Bad Request', 403
            return func(*args, **kwargs)
        return decorated_function
    return decorator
