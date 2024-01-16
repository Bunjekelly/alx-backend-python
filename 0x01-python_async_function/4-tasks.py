#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""

import random
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async coroutine"""
    list1 = []
    for _ in range(n):
        list1.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*list1))
