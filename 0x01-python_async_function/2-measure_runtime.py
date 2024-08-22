#!/usr/bin/env python3
"""Asyncs basics"""
from time import time
from asyncio import run

def measure_time(n: int, max_delay: float) -> float:
    """measure run time"""
    start = time()
    run(wait_n(n, max_delay))
    end = time()

    return (end - start) / n

