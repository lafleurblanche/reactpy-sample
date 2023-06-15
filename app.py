from fastapi import FastAPI
from uvicorn import run
from reactpy import component, html
from reactpy.backend.fastapi import configure, Options

def Head():
    return (
        html.link(
            {
                "href": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
                "rel": "stylesheet",
            }
        ),
        html.script({"src": "https://cdn.tailwindcss.com"}, ""),
    )


@component
def Root():
    return html._(
        html.h1(
            "Hello, world!",
        ),
        html.p(
            "Hello, world!",
        ),
    )

app = FastAPI()

configure(
    app,
    Root,
    Options(head=Head()),
)

if __name__ == "__main__":
    run(app)
