#Получить имя, цену и ссылку на светильники
import scrapy


class Ps05LightParsSpider(scrapy.Spider):
    name = "PS05_light_pars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # код для парсера
        # в эту пременную будут сохраняться все карточки со светильниками
        lights = response.css('div._Ud0k')
        # Поработаем с каждым светильником
        # из класса где есть имя name , ищем тег span и берем из него только текст
        # и берем первый поавшийся элемент .get()
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.pY3d2 span::text').get(),
                # для ссылки ищем тег a и атрибут href
                'url': light.css('a').attrib['href']
            }
