from selenium import webdriver


def get_actors(url):
    browser = webdriver.Firefox(executable_path=r'C:\\geckodriver.exe')
    browser.get(url)
    # находим все элементы по имени класса 'styles_list__I97eu' и далее в цикле вытаскиваем актеров и
    # записываем их в список
    elements = browser.find_elements_by_class_name('styles_list__I97eu')
    actors = []
    for elem in elements:
        actors += elem.text.split('\n')
    return actors


get_actors('https://www.kinopoisk.ru/film/42326/')
get_actors('https://www.kinopoisk.ru/film/326/')
