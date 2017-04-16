# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from datetime import datetime
from pyvirtualdisplay import Display

def setUp():
    display = Display(visible=0, size=(800, 600))
    display.start() # for server should be uncomented
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    return driver

def scroll(driver):
    element = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div/div/div[1]/fieldset/div[2]/div/div[3]')
    driver.execute_script("arguments[0].setAttribute('class','ps-active-y')", element)

def set_departure(driver, departure_airport):
    driver.find_element_by_xpath('//*[@id="search-departure-station"]').send_keys(departure_airport)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div/div/div[1]/fieldset/div[2]/div/div[3]/div[1]/label/strong').click()
    sleep(2)

def set_arrival(driver, arrival_airport):
    driver.find_element_by_xpath('//*[@id="search-arrival-station"]').send_keys(arrival_airport)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div/div/div[1]/fieldset/div[2]/div/div[3]/div[1]/label/small').click()
    sleep(2)

def button_click(driver):
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div/div/div[1]/div[2]/button').click()
    sleep(2)
    select = Select(driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div[2]/div[1]/div[1]/div/select'))
    select.select_by_visible_text(u'травень 2017')
    sleep(2)

def show_time(driver):
    if driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div[2]/div[1]/div[2]/div/button').text == u"ПОКАЗАТИ ЧАС ВІДПРАВЛЕННЯ":
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div[2]/div[1]/div[2]/div/button').click()
        sleep(2)

def clear_departure_airport(driver):
    driver.find_element_by_xpath('//*[@id="search-departure-station"]').clear()

def get_airports_list(driver):
    return (driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/main/div/div/div[2]/div/div/div[1]/fieldset/div[2]/div').text).split('\n')[1:]

def get_normal_date(date, time):
    hours, minutes = time.split(":")
    return datetime(int(2017), int(5), int(date), int(hours), int(minutes))
