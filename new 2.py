import time

import telebot
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



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
bot = telebot.TeleBot(API_KEY)



@bot.message_handler(commands=["start", "help"])
def handle_start_help(message):
    text = bot.send_message(message.chat.id,"Здравствуй уважаемый пользователь.\n" \
           "Список доступных команд:\n" \
           "/l - введите логин \n" \
           "/p - введите пароль \n" \
           "/s - поиск \n" \
           "/help, /start - помощь по боту.")
    bot.register_next_step_handler(text, login)

def login(message):
    if message.text == '/l':
        bot.send_message(message.chat.id, "Введите логин")
        browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
        email_input = browser.find_element(By.ID, 'b-domik_popup-username')
        email_input.clear()
        email_input.send_keys(message.text)
        msg = bot.send_message(message.chat.id, 'Введите команду /p')
        bot.register_next_step_handler(msg, password)
    else:
        bot.send_message(message.chat.id, 'Такой команды не существует, введите /start или /help')

def password(message):
    if message.text == '/p':
        browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
        passwor_input = browser.find_element(By.ID,'b-domik_popup-password')
        passwor_input.clear()
        passwor_input.send_keys(message.text)
        passwor_input.send_keys(Keys.ENTER)
        msg = bot.send_message(message.chat.id, 'Введите команду /s')
        bot.register_next_step_handler(msg, search)
    else:
        bot.send_message(message.chat.id, 'Такой команды не существует, введите /start или /help')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Такой команды не существует, введите /start или /help')

def search(message):
    if message.text == '/s':
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
    else:
        bot.send_message(message.chat.id, 'Такой команды не существует, введите "/start" или "/help"')



bot.polling()