from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOOK_FILE_PATH = 'arman_book.pdf'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome! Use /download to get the book.')

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open(BOOK_FILE_PATH, 'rb') as book_file:
        await update.message.reply_document(book_file, filename='Your_Book_Title.pdf')  # Change the filename as needed

def main() -> None:
    application = ApplicationBuilder().token('7279688109:AAGp4ZZjdYo9Zo9ueRwKtj69po7PnGL4YCo').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('download', download))

    application.run_polling()

if __name__ == '__main__':
    main()
