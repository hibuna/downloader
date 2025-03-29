import json
import logging
from functools import wraps
from typing import Iterable

from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def log_transform(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log_args(args[1:], kwargs, prefix="Input ")
            result = func(*args, **kwargs)
            log_args(args[1:], kwargs, prefix="Output ")
            return result
        except Exception as e:
            logger.exception(
                f"Exception raised in {func.__name__}. exception: {str(e)}"
            )
            raise e

    return wrapper


def log_args(args: Iterable, kwargs: dict = None, prefix: str = None) -> None:
    prefix = prefix or ""

    for i, arg in enumerate(args):
        if isinstance(arg, BaseModel):
            arg = arg.model_dump()

        logging.info(f"{prefix} argument: {i} -> {json.dumps(arg)}")

    for key, value in kwargs.items():
        if isinstance(key, BaseModel):
            key = key.model_dump()

        if isinstance(value, BaseModel):
            value = value.model_dump()

        logging.info(f"{prefix} kwarg key: {json.dumps(key)}")
        logging.info(f"{prefix} kwarg value: {json.dumps(value)}")
