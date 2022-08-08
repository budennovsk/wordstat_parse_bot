import telebot
import main_tg
API_KEY = '5465489989:AAGMpca8ww7GmlcF2ofDxFLO_qTZtliUUpM'


bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['старт'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['поиск'])
def search_ya(message):
    msg = bot.send_message(message.chat.id, "Введите текст для поиска")
    bot.register_next_step_handler(msg, search)

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Чо хотел")

def search(message):
    bot.send_message(message.chat.id, main_tg.res)


bot.polling()