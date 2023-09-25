---
layout: assignment-two-column
title: AsyncIO, FastAPI, and Python
type: lab
draft: 1
points: 6
abbreviation: Lab 5
show_schedule: 1
num: 5
start_date: 2023-09-28
due_date: 2023-10-05
---

## 1. Reading & Reference Materials
* AsyncIO
* Python Reference
* FastAPI

## 2. Introduction to AsyncIO
{:.blockquote-no-margin}
> **Note: This tutorial was generated with the help of ChatGPT!**

The `asyncio` module in Python is a powerful library that provides a framework for writing asynchronous, concurrent code using the `async` and `await` syntax. Asynchronous programming allows you to write programs that can perform multiple tasks concurrently without blocking the main execution thread, making it particularly useful for I/O-bound and network-bound operations.

In this tutorial, we will cover the following topics:

1. [What is asyncio?](#step1)
1. [Basic Concepts](#step2)
1. [Getting Started with asyncio](#step3)
1. [Defining a coroutine with async](#step4)
1. [Running multiple coroutines at once](#step5)
1. [Using asyncio with I/O Operations](#step6)
1. [Error Handling](#step7)
1. [Timeouts and Cancellation](#step8)
1. [Real-World Example: Fetching Multiple URLs](#step9)
1. [Conclusion and Further Resources](#step10)

{:#step1}
### 1. What is asyncio?
asyncio is a Python library that provides a framework for asynchronous programming. It is designed to handle concurrent I/O operations efficiently and is particularly useful for network programming, web scraping, and other tasks where you might otherwise be waiting for data to arrive.

{:#step2}
### 2. Basic Concepts
Before diving into asyncio, it's essential to understand some basic concepts:

* **Coroutines**: Coroutines are special functions defined with the async keyword. They can be paused and resumed, allowing non-blocking execution of tasks.
* **Event Loop**: An event loop is the core component of asyncio. It manages and schedules the execution of coroutines.
* **Tasks**: Tasks represent units of work in asyncio. You can create and manage multiple tasks within an event loop.

{:#step3}
### 3. Getting Started with asyncio
To use `asyncio`, you need Python 3.5 or later. Most modern Python installations come with asyncio built-in, so you don't need to install it separately.

{:#step4}
### 4. Defining a coroutine with async
To create a coroutine, use the `async` keyword:

```python
import asyncio

async def my_coroutine():
    print("Hello, asyncio!")

# To run a coroutine, you need an event loop.
loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
loop.close()
```

{:#step5}
### 5. Running multiple asynchronous coroutines at once
You can create and run tasks concurrently:

```python
import asyncio


async def coroutine1():
    await asyncio.sleep(3)
    print("Coroutine 1 completed")
    return 6  # fake data to be returned


async def coroutine2():
    await asyncio.sleep(1.5)
    print("Coroutine 2 completed")
    return 9  # fake data to be returned


async def main():
    result1, result2 = await asyncio.gather(coroutine1(), coroutine2())

    # Note that the statements below only execute once both
    # coroutines have executed. This is because of the "await"
    # keyword.
    print(result1)
    print(result2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

```

* `asyncio.gather` -- a function in the asyncio library -- allows you to concurrently execute multiple coroutines and collect their results. It's a way to run multiple asynchronous tasks concurrently and wait for all of them to complete.
* `asyncio` also has an event loop that manages coroutine execution:

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
loop.close()
```


{:#step6}
### 6. Using asyncio with I/O Operations
`asyncio` excels at I/O-bound operations. Here's an example of reading files asynchronously:

```python
import asyncio

async def read_file(filename):
    async with open(filename, 'r') as file:
        content = await file.read()
        print(f"Read {len(content)} characters from {filename}")

loop = asyncio.get_event_loop()
loop.run_until_complete(read_file('example.txt'))
loop.close()
```

{:#step7}
### 7. Error Handling
Use try and except to handle errors within coroutines:

```python
import asyncio

async def my_coroutine():
    try:
        # Your code here
    except Exception as e:
        print(f"An error occurred: {e}")

loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
loop.close()
```

{:#step8}
### 8. Timeouts and Cancellation
asyncio allows you to set timeouts and cancel tasks:

```python
import asyncio

async def timeout_task():
    try:
        await asyncio.wait_for(long_running_task(), timeout=1)
    except asyncio.TimeoutError:
        print("Task timed out")

loop = asyncio.get_event_loop()
loop.run_until_complete(timeout_task())
loop.close()
```
{:#step9}
### 9. Real-World Example: Fetching Multiple URLs
Here's a simple example of fetching multiple URLs concurrently using aiohttp:

```python
import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com", "https://openai.com"]
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, result in zip(urls, results):
        print(f"Fetched {len(result)} bytes from {url}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

{:#step10}
### 10. Conclusion and Further Resources
This tutorial provides a basic introduction to the asyncio module in Python. Asynchronous programming can significantly improve the performance of I/O-bound tasks and concurrent operations. To dive deeper into asyncio, explore the official documentation and try building more complex applications.

Official asyncio documentation: <a href="https://docs.python.org/3/library/asyncio.html" target="_blank">https://docs.python.org/3/library/asyncio.html</a>

Remember that asynchronous programming can be complex, so practice and experimentation are essential for mastering it.

## 3. Set Up

* Same as **app**, but downgraded the python dependency to >= 3.7. Note that asyncio was introduced to Python in version 3.5.
* TODO: Copy from Semmy's `README.md` instructions

## 4. Your Tasks