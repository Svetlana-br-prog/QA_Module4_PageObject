class BasePage():
# В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
# Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)