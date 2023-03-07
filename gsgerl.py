# модуль голсовые сообщения девушек
# подпишись на тг канал @modwini
from .. import loader


@loader.tds
class voiceGirls(loader.Module):
    """Голосовые сообщения девушек by @modwini"""

    strings = {"name": "voiceGirls"}

    async def hicmd(self, message):
        """Приветик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/195",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def cdcmd(self, message):
        """Как дела?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/198",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def yescmd(self, message):
        """Да"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/197",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def nocmd(self, message):
        """Нет"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/196",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def oj(self, message):
        """очень жаль"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/199",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def nedoveraycmd(self, message):
        """я тебе не доверяю"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/200",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def podcmd(self, message):
        """подожди"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/201",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def gncmd(self, message):
        """спокойной ночи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/202",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def iscmd(self, message):
        """ясно"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/203",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def obidcmd(self, message):
        """я обиделась"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/204",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ilovecmd(self, message):
        """ты мне нравишся"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/205",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def murcmd(self, message):
        """мур"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/206",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def pjcmd(self, message):
        """ну пожалуйста"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/207",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def thancmd(self, message):
        """спасибо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/208",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
