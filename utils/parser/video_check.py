import asyncio
from .parser import youtube_get_information
from ..db_api import db_funcs


async def periodic():
    pass


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

