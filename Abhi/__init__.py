"""
Telegram @Itz_Your_4Bhi
Copyright ©️ 2025
"""

import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import GroupCallParticipant

from Player.Core.Bot import MusicBot, MusicUser
from .Logging import LOGGER
from Abhi.Misc import sudo

sudo()

app = MusicBot
call = MusicUser


seek_chats = {}

import unittest
from Abhi.Test import greet

class TestExamplePlugin(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Abhi"), "Hello, Abhi! This is a plugin.")

if __name__ == '__main__':
    unittest.main()
