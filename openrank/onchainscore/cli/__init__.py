import asyncio
from functools import wraps
from typing import Optional, Annotated

import typer


def sync(f):
    """Decorate an async function to turn it into a synchronous one.

    Done by running the function in the default asyncio loop.

    Use this, e.g. to decorate an asynchronous function to use it as
    a Click/Typer command function.
    """

    @wraps(f)
    def wrapper(*poargs, **kwargs):
        return asyncio.run(f(*poargs, **kwargs))

    return wrapper


app = typer.Typer()


@app.command()
def version():
    from .. import __version__
    print(f"openrank-onchain-score {__version__}")


def entrypoint():
    return app()
