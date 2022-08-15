import telebot
import main_tg
API_KEY = '5527701613:AAGkNjE8XJFgcpE2_BB6FN3otNFjG0MnxIw'


bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['старт'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['поиск'])
def search_ya(message):
    msg = bot.send_message(message.chat.id, "Введите текст для! ")
    bot.register_next_step_handler(msg, search)

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Чо??")

def search(message):
    bot.send_message(message.chat.id, main_tg.res)


bot.polling()