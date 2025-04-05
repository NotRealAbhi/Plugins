"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""

from .Logging import *
from .Misc import *
from .Utils import *
from .Core import *
from .Plugins import *


sudo()

app = MusicBot
call = MusicUser


seek_chats = {}



def greet(name: str) -> str:
    return f"Hello, {name}! This is a plugin."
