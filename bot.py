import telebot

# التوكن ديالك اللي عطيتيني
TOKEN = '8038038213:AAF_41SBVowk0KaSAqrVQaV9H9yMAf5sldU'
bot = telebot.TeleBot(TOKEN)

# الـ ID ديالك باش يصيفط ليك أنتِ بوحدك
MY_CHAT_ID = '6683842631'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(MY_CHAT_ID, "✅ أهلاً Mita! البوت System Watcher دابا خدام ومربوط بحسابك 24/24 ساعة على سيرفر Koyeb.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "راني خدام وكنسمعك مزيان!")

print("البوت بدأ العمل بنجاح...")
bot.polling()
