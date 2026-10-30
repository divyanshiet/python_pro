import asyncio,time

# def as_task1(delay_duration: int):
#     print("Sync Task 1 started")
#     time.sleep(delay_duration)

# def as_task2(delay_duration: int):
#     print("Sync Task 2 started")
#     time.sleep(delay_duration)

# def as_task3(delay_duration: int):
#     print("Sync Task 3 started")
#     time.sleep(delay_duration)

# def as_task4(delay_duration: int):
#     print("Sync Task 4 started")
#     time.sleep(delay_duration)

# def sync_version():
#     as_task1(1)
#     as_task2(2)
#     as_task3(1)
#     as_task4(3)


# async def task1(delay_duration: int):
#     print("Task 1 started")
#     await asyncio.sleep(delay_duration)

# async def task2(delay_duration: int):
#     print("Task 2 started")
#     await asyncio.sleep(delay_duration)

# async def task3(delay_duration: int):
#     print("Task 3 started")
#     await asyncio.sleep(delay_duration)

# async def task4(delay_duration: int):
#     print("Task 4 started")
#     await asyncio.sleep(delay_duration)

# async def main2():
#     await asyncio.gather(
#         task1(1),
#         task2(2),
#         task3(1),
#         task4(3)
#     )

# def async_await():
#     sync_version()
#     asyncio.run(main2())


## Error handling: make one of the four calls raise a ValueError. 
## Use gather(..., return_exceptions=True) and print the successful results 
## and the failures separately, with the index of each failure.

# async def task1(delay_duration: int):
#     print("Task 1 started")
#     await asyncio.sleep(delay_duration)

# async def task2(delay_duration: int):
#     print("Task 2 started")
#     await asyncio.sleep(delay_duration)

# async def task3(delay_duration: int):
#     if delay_duration != 3:
#         raise ValueError(f"Incorrect delay duration: {delay_duration}")
#     else:
#         print("Task 3 started")
#     await asyncio.sleep(delay_duration)

# async def task4(delay_duration: int):
#     print("Task 4 started")
#     await asyncio.sleep(delay_duration)

# async def main2():
#     results = await asyncio.gather(
#         task1(1),
#         task2(2),
#         task3(1),
#         task4(3),
#         return_exceptions=True
#     )
#     for i, r in enumerate(results):
#         if isinstance(r, Exception):
#             print(f"call {i} failed: {r}")
#         else:
#             print(f"call {i} gave {r}")

# def async_await():
#     asyncio.run(main2())

## Semaphore: run 6 calls of 1 second each with Semaphore(2). 
## Print start and done messages, and confirm only 2 run at a time and the total is about 3 seconds.
## Then change the limit to 3 and predict the new total.

# async def task1(delay_duration:int,semaphore):
#     async with semaphore:
#         print(f"Task 1 started")
#         await asyncio.sleep(2)
#         print(f"Task 1 completed")

# async def task_call():
#     semaphore = asyncio.Semaphore(2)
#     await asyncio.gather(*(task1(1,semaphore) for i in range(0,6)))

# async def task_call_three():
#     semaphore = asyncio.Semaphore(3)
#     await asyncio.gather(*(task1(1,semaphore) for i in range(0,6)))

# def async_await():
#     asyncio.run(task_call())
#     asyncio.run(task_call_three())

# Timeout: write an async helper that takes a name and a delay, and wraps the sleep 
# in asyncio.wait_for(..., timeout=2). Run calls with delays of 1 and 5 concurrently, 
# catching asyncio.TimeoutError inside the helper, so one timeout doesn’t affect the other call.
# Print which succeeded and which timed out.

async def task1(task_name:str,delay_duration:int):
    try:
        await asyncio.wait_for(asyncio.sleep(delay_duration),timeout=2)
        print(f"{task_name}: Completed (delay = {delay_duration})")
    except asyncio.TimeoutError:
        print(f"{task_name}: Timeout (delay = {delay_duration}, timeout=2s)")


async def task_call():
    result = await asyncio.gather(task1("delay_1",1),task1("delay_5",5),return_exceptions=True)


def async_await():
    asyncio.run(task_call())