#!/usr/bin/env python3
"""Basics of async"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: float) -> float:
    """Implements task_wait_n that spawns task_wait_random
    n times
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.is_completed(tasks)]