from school_app.models import Student
from school_app.utils import average
from school_app.async_await import async_await
from school_app.httpx_check import httpx_call
import asyncio

def main() -> None:
    students = [Student(name="Asha", marks=85), Student(name="Ravi", marks=92)]
    # asyncio.run(main2())
    # async_await()
    asyncio.run(httpx_call())