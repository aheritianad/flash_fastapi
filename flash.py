from fastapi import Request
from enum import Enum


class Category(str, Enum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


def flash(request: Request, message: str, category: Category = Category.INFO):
    flashes = request.session.get("flashes", [])
    flashes.append({"message": message, "category": category.value})
    request.session["flashes"] = flashes


def get_flashed_messages(request: Request) -> list[dict[str, str]]:
    return request.session.pop("flashes", [])
