import time

import telebot
<<<<<<< HEAD
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from telebot import types # для указание типов
from selenium.webdriver.common.by import By

from fake_useragent import UserAgent



useragent = UserAgent()

options = webdriver.ChromeOptions()

# убирает надпись автоматическое тестоевое ПО
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# изменяет мой юзер агент с использованием рандома и библиотеки
options.add_argument(f'user-agent={useragent.random}')
browser = webdriver.Chrome(options = options)

browser.get('https://wordstat.yandex.ru/')
URL = browser.get('https://wordstat.yandex.ru/')


# аунтефикация через токен бота
API_KEY = '5465489989:AAGMpca8ww7GmlcF2ofDxFLO_qTZtliUUpM'
=======
import main_tg
API_KEY = '5527701613:AAGkNjE8XJFgcpE2_BB6FN3otNFjG0MnxIw'


>>>>>>> 146a201e2e6f0b9a1574a9e2faeda780c2638d61
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("✏ Ввести логин")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Здравствуй {0.first_name}! Мы сделали этот бот для того, чтобы каждый мог без труда пользоваться статистикой ключевых слов Yandex WordStat. Для того, чтобы приступить к использованию бота требуется авторизоваться в учетной записи Yandex".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "✏ Ввести логин"):
        msg = bot.send_message(message.chat.id, "Введите ваш логин от учетной записи Yandex")
        bot.register_next_step_handler(msg, login, )
    elif(message.text == "❓ Задать вопрос"):
        bot.send_message(message.chat.id, text="О чем поговорим?")
        # bot.register_next_step_handler(comm, login, ) Здесь надо допилить функцию сохранения комментария

def login(message):
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    email_input = browser.find_element(By.ID, 'b-domik_popup-username')
    email_input.clear()
    email_input.send_keys(message.text)
    msg = bot.send_message(message.chat.id, "Введи пароль. Введя свои личный данный в нашем боте вы принимаете соглашение об обработке персональных данных, переданными вами. В свою очередь мы обещаем использовать их только для входа в сервис и не будем передавать третьим лицам.")
    bot.register_next_step_handler(msg, password)



def password(message):
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    passwor_input = browser.find_element(By.ID,'b-domik_popup-password')
    passwor_input.clear()
    passwor_input.send_keys(message.text)
    passwor_input.send_keys(Keys.ENTER)
    # Нужно добавить функцию ввода неправильного пароля и ссылаться на возврат к последним 2 строчкам функции login

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "🔍 По словам"):
        otvet = bot.send_message(message.chat.id, "Введите текст для поиска")
        bot.register_next_step_handler(otvet, search)

    elif (message.text == "Настроить параметры"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("По регионам")
        btn2 = types.KeyboardButton("История запросов")
        btn3 = types.KeyboardButton("Настройка региона")
        back = types.KeyboardButton("Вернуться назад")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выбери вариант", reply_markup=markup)

    elif (message.text == "По регионам"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "История запросов":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif message.text == "Настройка региона":
        bot.send_message(message.chat.id, text=" ")

    # Надо понять как сослаться назад на функцию
    # elif (message.text == "Вернуться назад"):
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     button1 = types.KeyboardButton("👋 Поздороваться")
    #     button2 = types.KeyboardButton("❓ Задать вопрос")
    #     markup.add(button1, button2)
    #     bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    # else:
    #     bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Для поиска введи значение /s")

def search(message):
    driver = browser.find_element(By.CLASS_NAME, 'b-form-input__input')
    driver.clear()
    driver.send_keys(message.text)
    time.sleep(3)
    driver.send_keys(Keys.ENTER)
    time.sleep(3)
    blocks = browser.find_element(By.CLASS_NAME,'b-word-statistics__table')
    all_blocks = blocks.find_elements(By.CSS_SELECTOR, 'td[class*="b-word-statistics__td"]')
    for i in (all_blocks)[:6]:
        bot.send_message(message.chat.id, i.text)


bot.polling()
