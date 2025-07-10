# async_utils.py

import asyncio

async def async_add(a, b):
    await asyncio.sleep(0.1)
    return a + b
