from pyrogram import Client, Filters

from khamiss import (HELP_STICKER, MSAADA_TXT, TMP_DOWNLOAD_DIRECTORY)


@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)
