#!/usr/bin/env python3
"""Basics of async"""
import random


async def wait_random(max_delay: float) -> float:
    """Implements wait_random async function
    """
    return await random.uniform(0, max_delay)