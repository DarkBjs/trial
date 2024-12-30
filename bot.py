import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Add your Telegram bot token here
BOT_TOKEN = '7484144335:AAERDaK-VfcmaJGYFYIADKdmnzXuhyT-OUI'

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Function to show the keyboard
def show_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    # Add buttons to the layout
    markup.row(
        KeyboardButton("🏅Pʀᴏᴍᴏᴛᴇʀ Cʜᴀɴɴᴇʟ")
    )
    markup.row(
        KeyboardButton("➕Aᴅᴅ Mʏ Cʜᴀɴɴᴇʟ")
    )
    markup.row(
        KeyboardButton("🛡️Mʏ Wᴀʟʟᴇᴛ")
    )
    markup.row(
        KeyboardButton("📞Cᴏɴᴛᴀᴄᴛ Us"),
        KeyboardButton("👥Aʙᴏᴜᴛ Us")
    )

    # Send only the keyboard and the welcome message with first name
    first_name = message.chat.first_name
    bot.send_message(
        message.chat.id,
        f"*😇 Wᴇʟᴄᴏᴍᴇ {first_name} Bᴜᴅᴅʏ Tᴏ Lᴇxᴀ Pʀᴏᴍᴏ*",
        reply_markup=markup,
        parse_mode='Markdown'
    )

# Command handler for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    show_menu(message)

print("Bot is running...")
bot.polling()
