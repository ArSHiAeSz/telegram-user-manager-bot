from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from database import create_table, add_user, user_exists

TOKEN = "توکن_ربات_خودت"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋\nبرای ثبت نام /register رو بزن")

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_id = user.id
    name = user.full_name

    if user_exists(user_id):
        await update.message.reply_text("❌ قبلاً ثبت نام کردی")
        return

    add_user(user_id, name)
    await update.message.reply_text("✅ ثبت نام انجام شد")

def main():
    create_table()  # دیتابیس آماده میشه

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))

    app.run_polling()

if __name__ == "__main__":
    main()
