from selene import browser, by

class MainPageObjects:
    def __init__(self):
        self.submit_application = browser.element('.head-section__main > div > button')
        self.connection = browser.element(by.text('Подключение'))
        self.career = browser.element(by.text('Карьера'))
        self.about_company = browser.element(by.text('О нас'))
        self.blog = browser.element(by.text('Блог'))
        self.contacts = browser.element(by.text('Контакты'))
        self.sign_in = browser.element(by.text('Вход'))

class ConsultationForm:



    def open(self):
        browser.open('/')


