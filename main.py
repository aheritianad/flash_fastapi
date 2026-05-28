from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from flash import flash, get_flashed_messages, Category

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-key",
)


@app.get("/")
def test(request: Request):
    flash(request, message="Hello world!", category=Category.INFO)
    flashes = get_flashed_messages(request)
    return flashes
