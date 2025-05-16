import os
import logging
from downloader import download_media
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /video or /audio followed by a link.")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cmd = update.message.text.split()
    if len(cmd) < 2:
        return await update.message.reply_text("Usage: /video <url> or /audio <url>")

    media_type = cmd[0][1:]  # removes the '/' from command
    url = cmd[1]

    await update.message.reply_text("Downloading, please wait...")
    filepath = download_media(url, media_type)

    with open(filepath, 'rb') as f:
        if media_type == "audio":
            await update.message.reply_audio(f)
        else:
            await update.message.reply_video(f)

    os.remove(filepath)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("video", download))
app.add_handler(CommandHandler("audio", download))

app.run_polling()
