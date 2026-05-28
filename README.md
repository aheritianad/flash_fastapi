# flash_fastapi

A lightweight Flask-style flash messaging utility for FastAPI applications.

`flash_fastapi` provides a simple way to store temporary messages in the user session and retrieve them on the next request. It is useful for:

- Form submission feedback
- Success/error notifications
- Redirect messages
- HTMX interactions
- Server-rendered FastAPI applications using Jinja2

Repository: [flash_fastapi GitHub Repository](https://github.com/aheritianad/flash_fastapi?utm_source=chatgpt.com)

---

## Features

- Flask-like `flash()` API
- Session-based message storage
- Message categories (`info`, `success`, `warning`, `error`)
- Works with FastAPI and Starlette sessions
- Minimal and dependency-light

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aheritianad/flash_fastapi.git
cd flash_fastapi
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

You also need Starlette session middleware:

```bash
pip install itsdangerous
```

---

## Project Structure

```text
flash_fastapi/
├── flash.py
└── main.py
```

---

## Usage

### 1. Enable Session Middleware

```python
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-key",
)
```

---

### 2. Import Flash Utilities

```python
from flash import flash, get_flashed_messages, Category
```

---

### 3. Flash a Message

```python
flash(request, message="Saved successfully", category=Category.SUCCESS)
```

Available categories:

```python
Category.INFO
Category.SUCCESS
Category.WARNING
Category.ERROR
```

---

### 4. Retrieve Messages

```python
flashes = get_flashed_messages(request)
```

Messages are automatically removed from the session after retrieval.

Example output:

```python
[
    {
        "message": "Saved successfully",
        "category": "success"
    }
]
```

---

## Full Example

```python
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

from flash import flash, get_flashed_messages, Category

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-key",
)


@app.get("/")
def home(request: Request):
    flash(
        request,
        message="Hello world!",
        category=Category.INFO,
    )

    flashes = get_flashed_messages(request)

    return flashes
```

---

## Using With Jinja2 Templates

Example with Bootstrap alerts:

```html
{% if flashes %}
    {% for flash in flashes %}
        <div class="alert alert-{{ flash.category }}">
            {{ flash.message }}
        </div>
    {% endfor %}
{% endif %}
```

Example route:

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    flash(request, "Welcome back!", Category.SUCCESS)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "flashes": get_flashed_messages(request)
        }
    )
```

---

## API Reference

### `flash(request, message, category=Category.INFO)`

Adds a flash message to the session.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `request` | `Request` | FastAPI request object |
| `message` | `str` | Message content |
| `category` | `Category` | Message type |

---

### `get_flashed_messages(request)`

Retrieves and clears all flash messages from the session.

#### Returns

```python
list[dict[str, str]]
```

---

## Categories

| Category | Purpose |
|---|---|
| `INFO` | General information |
| `SUCCESS` | Successful actions |
| `WARNING` | Warnings |
| `ERROR` | Errors and failures |

---

## Example Response

```json
[
  {
    "message": "Hello world!",
    "category": "info"
  }
]
```

---

## Future Improvements

Possible future enhancements:

- Package publishing on PyPI
- Typed message models
- Middleware helpers
- Automatic template integration
- Async utilities
- HTMX helper functions

---

## License

MIT License.

---

## Author

Created by entity["people","Heritiana Daniel Andriasolofo","GitHub developer"].
