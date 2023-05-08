import time

import telebot
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

from selenium.webdriver.common.by import By

from fake_useragent import UserAgent

# создание феиковых хендлеров браузера
useragent = UserAgent()
# выбор брайзера для парсинга
options = webdriver.ChromeOptions()

# убирает надпись автоматическое тестоевое ПО
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# изменяет мой юзер агент с использованием рандома и библиотеки
options.add_argument(f'user-agent={useragent.random}')
browser = webdriver.Chrome(options=options)
# подключение
URL = browser.get('https://wordstat.yandex.ru/')

# токен авторизации телеграмм
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    """ Старт """
    bot.send_message(message.chat.id, "Здравствуйте, для аунтефикаций на wordstat.ru введите команду /l ")

@bot.message_handler(commands=["start", "help"])
def handle_start_help(message: telebot.types.Message):
    """ Хелпер """
    text = "Здравствуй уважаемый пользователь.\n" \
           "Список доступных команд:\n" \
           "/l - введите логин \n" \
           "/p - введите пароль \n" \
           "/s - поиск \n" \
           "/help, /start - помощь по боту."
    bot.reply_to(message, text)


@bot.message_handler(commands=["l"])
def log(message):
    """ ВВод логина на вордстате через телеграм"""
    if message.text == '/l':
        msg = bot.send_message(message.chat.id, "Введи логин")
        bot.register_next_step_handler(msg, login)
    else:
        bot.send_message(message.chat.id, 'error')


def login(message):
    """ Обработка селениумом логина"""
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    email_input = browser.find_element(By.ID, 'b-domik_popup-username')
    email_input.clear()
    email_input.send_keys(message.text)


@bot.message_handler(commands=["p"])
def pas(message):
    """ ВВод логина на вордстате через телеграм"""
    msg = bot.send_message(message.chat.id, "Введи пароль")
    bot.register_next_step_handler(msg, password)


def password(message):
    """ Обработка селениумом логина"""
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    passwor_input = browser.find_element(By.ID, 'b-domik_popup-password')
    passwor_input.clear()
    passwor_input.send_keys(message.text)
    passwor_input.send_keys(Keys.ENTER)


@bot.message_handler(commands=["s"])
def sear(message):
    """ ВВод поиска в вордстате через телеграм"""
    answer = bot.send_message(message.chat.id, "Введите текст для поиска")
    bot.register_next_step_handler(answer, search)


@bot.message_handler(content_types=['text'])
def text(message):
    """ Ввод поиска """
    bot.send_message(message.chat.id, "Для поиска введи значение /s")


def search(message):
    """ Поиск по заголовкам в вордатсате с выводом в телеграм 6 часто используемых слов"""
    driver = browser.find_element(By.CLASS_NAME, 'b-form-input__input')
    driver.clear()
    driver.send_keys(message.text)
    time.sleep(3)
    driver.send_keys(Keys.ENTER)
    time.sleep(3)
    blocks = browser.find_element(By.CLASS_NAME, 'b-word-statistics__table')
    all_blocks = blocks.find_elements(By.CSS_SELECTOR, 'td[class*="b-word-statistics__td"]')
    for i in (all_blocks)[:6]:
        bot.send_message(message.chat.id, i.text)


if __name__ == "__main__":
    try:
        bot.polling()
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")

