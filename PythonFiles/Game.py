import discord
import discord
import asyncio
import sqlite3
from discord.ext import commands


class game(commands.Cog):

    class Animated:
        def __init__(self, name, HP, max_HP, XP, defense, attack, gold, speed):
            self.name = name #name of the alive character
            self.HP = HP #current health point
            self.max_HP = max_HP #max health points
            self.XP = XP #xp
            self.defense = defense #defense (shielding)
            self.attack = attack #how hard you hit
            self.gold = gold #currency

    class Character(Animated):
        max_level = 20
        def __init__(self, name, HP, max_HP, XP, defense, attack, gold, w, armor, accessory, ctype, battling, mode, region, level, speed, user_id):
            super().__init__(name, HP, max_HP, XP, defense, attack, gold)
            self.w = w #weapon slot 1
            self.armor = armor
            self.accessory = accessory
            self.ctype = ctype #character type
            self.battling = battling #character battling
            self.mode = mode #gamemode
            self.region = region #biome
            self.level = level #level
            self.speed = speed #dodging chance
            self.user_id = user_id #user id

        @property
        def level(self):
            return self._level



