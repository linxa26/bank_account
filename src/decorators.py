from typing import Callable, TypeVar, Optional
from functools import wraps

R = TypeVar("R")


def log(filename: Optional[str] = None) -> Callable[[Callable[..., R]], Callable[..., R]]:
    """
    Декоратор для логирования выполнения функции.
    При успешном выполнении выводит сообщение "ok",
    при ошибке — сообщение "error" с деталями.
    Если указан filename, запись идет в файл, иначе — в консоль.
    """
    def decorator(func: Callable[..., R]) -> Callable[..., R]:

        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> R:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)

            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)

                raise

            return result

        return wrapper

    return decorator