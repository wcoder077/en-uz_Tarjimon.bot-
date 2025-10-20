import telebot  
from uz import words  

TOKEN = "7629404273:AAFBEGgdnpiW-iMHYJq0IgWf9YxQo1L0b7g"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    res = "Assalomu alaykum!\n"
    res += "Bu bot sizga o‘zbekcha va inglizcha so‘zlarni tarjima qilib beradi.\n"
    res += "Faqat so‘zni yozing 🙂"
    bot.reply_to(message, res)

@bot.message_handler(func=lambda message: True)
def translate_word(message):
    text = message.text.lower()
    translation = None

    # Tarjima qilish
    for word in words:
        if text == word["englishWord"].lower():
            translation = word["targetWord"]
            break
        elif text == word["targetWord"].lower():
            translation = word["englishWord"]
            break

    if translation:
        bot.reply_to(message, f"👉 {translation}")
    else:
        bot.reply_to(message, "😕 Bu so‘z lug‘atda topilmadi.")

bot.polling()
 