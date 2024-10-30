import telebot

API_TOKEN = '7658462934:AAHIZ8BujNDGdj16F86TpUIpJ6U0o6g0Sdo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "этот бот лежит на локальном сервере с автозапуском")


if __name__ == '__main__':
    bot.infinity_polling()
