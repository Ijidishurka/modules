# Канал - @modwini
from .. import loader
from asyncio import sleep


@loader.tds
class elpe(loader.Module):
    strings = {"name": "ЛП by @modwini"}

    @loader.owner
    async def elpecmd(self, message):
        for _ in range(1):
            for elpe in ["Крестики нолики❌",
"Две Миланы в домике🏚️",
"Укатились даже шарики за ролики🎱",
"Улы-улыбаемся, разгоняя тучки⛅",
"Люди обзываются что мы две почемучки😔",
"Отпути😤", "не путю😉",
"Но кому я говорю🤬",
"Не путю, ведь я люблю❤️",
"Свою лучшую подругу🤥",
"Отпути😶", "не путю😗",
"Но кому я говорю🙄",
"Не путю ведь я люблю💖",
"Навсегда мы друг для друга🥵",
"Элпе пе пе пе пе пе, пе пе🤤"]:
                await message.edit(elpe)
                await sleep(1.2)
