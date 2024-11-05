#файл divannewpars.py
#Получить имя, цену и ссылку на диваны

import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    #Та ссылка, от которой начинается парсинг.Заменили на диван и кресла
    #start_urls = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        #код для парсера
        #в эту пременную будут сохраняться все карточки с диванами
        divans = response.css('div._Ud0k')
        #Поработаем с каждым диваном
        #из класса где есть имя name , ищем тег span и берем из него только текст
        # и берем первый поавшийся элемент .get()
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                #для ссылки ищем тег a и атрибут href
                'url': divan.css('a').attrib['href']
            }

#--------------------
#scrapy.cfg
# Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.io/en/latest/deploy.html

[settings]
default = divanpars.settings
shell == ipython

[deploy]
#url = http://localhost:6800/
project = divanpars
