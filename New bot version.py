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



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте, для аунтефикаций на wordstat.ru введите команду /l ")
@bot.message_handler(commands=["start", "help"])
def handle_start_help(message: telebot.types.Message):
    text = "Здравствуй уважаемый пользователь.\n" \
           "Список доступных команд:\n" \
           "/l - введите логин \n" \
           "/p - введите пароль \n" \
           "/s - поиск \n" \
           "/help, /start - помощь по боту."
    bot.reply_to(message, text)

@bot.message_handler(func=lambda message: message.text == True)
def log(message):
    if message.text == '/l':
        msg = bot.send_message(message.chat.id, "Введи логин")
        bot.register_next_step_handler(msg, login)
    else:
        bot.send_message(message.chat.id, 'ff')

def login(message):
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    email_input = browser.find_element(By.ID, 'b-domik_popup-username')
    email_input.clear()
    email_input.send_keys('serega351351')



@bot.message_handler(func=lambda message: message.text == '/p')
def pas(message):
    msg = bot.send_message(message.chat.id, "Введи пароль")
    bot.register_next_step_handler(msg, password)


def password(message):
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    passwor_input = browser.find_element(By.ID,'b-domik_popup-password')
    passwor_input.clear()
    passwor_input.send_keys('.serega351..')
    passwor_input.send_keys(Keys.ENTER)

@bot.message_handler(func=lambda message: message.text == '/s')
def sear(message):
    answer = bot.send_message(message.chat.id, "Введите текст для поиска")
    bot.register_next_step_handler(answer, search)

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


if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")