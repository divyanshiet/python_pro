import asyncio
import time
from typing import TypedDict, cast

import httpx


class Todo(TypedDict):
    userId: int
    id: int
    title: str
    completed: bool


async def fetch_todo(client: httpx.AsyncClient, todo_id: int) -> Todo:
    response = await client.get(
        f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    )
    response.raise_for_status()
    return cast(Todo, response.json())


async def fetch_concurrently() -> None:
    start: float = time.perf_counter()

    async with httpx.AsyncClient(timeout=10.0) as client:
        todos: list[Todo] = await asyncio.gather(
            *(fetch_todo(client, todo_id) for todo_id in range(1, 11))
        )

    for todo in todos:
        print(todo["id"], todo["title"])

    elapsed: float = time.perf_counter() - start
    print(f"Concurrent fetch took {elapsed:.2f}s")


async def fetch_sequentially() -> None:
    start: float = time.perf_counter()
    todos: list[Todo] = []

    async with httpx.AsyncClient(timeout=10.0) as client:
        for todo_id in range(1, 11):
            todo: Todo = await fetch_todo(client, todo_id)
            todos.append(todo)

    for todo in todos:
        print(todo["id"], todo["title"])

    elapsed: float = time.perf_counter() - start
    print(f"Sequential fetch took {elapsed:.2f}s")


async def httpx_call() -> None:
    await fetch_concurrently()
    print()
    await fetch_sequentially()


asyncio.run(httpx_call())