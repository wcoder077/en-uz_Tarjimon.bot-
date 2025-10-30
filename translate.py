import os
from dotenv import load_dotenv
import telebot
from uz import words

# .env fayldan TOKEN ni o'qish
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    res = "Assalomu alaykum!\n"
    res += "Bu bot sizga o‘zbekcha va inglizcha so‘zlarni tarjima qilib beradi.\n"
    res += "Faqat so‘zni yozing 🙂"
    bot.send_message(message.chat.id, res)  # reply_to o'rniga send_message va chat.id


@bot.message_handler(func=lambda message: True)
def translate_word(message):
    text = message.text.lower()
    translation = None

    for word in words:
        if text == word["englishWord"].lower():
            translation = word["targetWord"]
            break
        elif text == word["targetWord"].lower():
            translation = word["englishWord"]
            break

    if translation:
        bot.send_message(message.chat.id, f"👉 {translation}")  # chat.id qo‘shildi
    else:
        bot.send_message(
            message.chat.id, "😕 Bu so‘z lug‘atda topilmadi."
        )  # chat.id qo‘shildi


bot.polling()
