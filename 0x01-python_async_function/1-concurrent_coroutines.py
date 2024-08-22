#!/usr/bin/env python3
"""Basics of async"""
import asyncio
import typing
wait_random = ('0-basic_async_function').wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """Implements wait n that spawns wait_random n times
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.is_completed(tasks)]