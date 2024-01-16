#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel using asyncio.gather
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """coroutine definition"""
    start = time.perf_counter()
    list1 = []
    for i in range(4):
        list1.append(async_comprehension())
    await asyncio.gather(*list1)
    end = time.perf_counter()
    return end - start
