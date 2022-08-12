import time

import telebot
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By


from auth import ya_password, ya_login
import pickle



browser = webdriver.Firefox()

browser.get('https://wordstat.yandex.ru')
URL = browser.get('https://wordstat.yandex.ru')


# API_KEY = '5465489989:AAGMpca8ww7GmlcF2ofDxFLO_qTZtliUUpM'
time.sleep(5)
def log(url, gg):
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()

    email_input = browser.find_element(By.ID,'b-domik_popup-username')
    email_input.send_keys(login_in())

#
# email_input = browser.find_element_by_id('b-domik_popup-password')
# email_input.send_keys(ya_password)
#
# xpath1 = '/html/body/form/table/tbody/tr[2]/td[2]/div/div[5]/span[1]/input'
# button1 = browser.find_element_by_xpath(xpath1).click()
#
# pickle.dump(browser.get_cookies(), open(f" {ya_login}_cookies", "wb"))
res = log(URL)

#
# def pasre(url):
#     for cookie in pickle.load(open(f" {ya_login}_cookies", "rb")):
#         browser.add_cookie(cookie)
#
#     time.sleep(4)
#     browser.refresh()
#     time.sleep(3)
#     search = browser.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr/td[4]/div/div/form/table/tbody/tr[1]/td[1]/span/span/input')
#     search.send_keys('vvv')
#     time.sleep(3)
#
#     browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[4]/div/div/form/table/tbody/tr[1]/td[2]/span/input').click()
#
#     time.sleep(3)
#     blocks = browser.find_elements(By.XPATH, '/html/body/div[2]/div/div/table/tbody/tr/td[4]/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/span/a')
#     # for i in blocks:
#     #     return (i.get_attribute('href'))
#     return [i.get_attribute('href') for i in blocks]
#         # responces =(i.get_attribute('href'))
#         # return responces
#
#     # blocks = browser.find_elements_by_tag_name('td')
#     # return (blocks)
#
#
# res = pasre(URL)





# blocks = browser.find_elements_by_tag_name('td')
# print(blocks)

#####################пишим бота############3

# bot = telebot.TeleBot(API_KEY)
# @bot.message_handlers(commands=['начать'])
#
# def hello(message):
#     bot.send_message(message.chat.id, 'Введите логин и пароль')
# bot.polling()

