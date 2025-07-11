# test_async_utils.py

import pytest
from async_utils import async_add

@pytest.mark.asyncio
async def test_async_add():
    result = await async_add(1, 2)
    assert result == 3
