# -*- coding UTF-8 -*-
# ИНФОРМАЦИЯ БЫЛА ПОЛУЧЕНА ОТ PHONERADAR.RU
# NOBLACK-MAIL НИКАК НЕ УЧАСТВУЕТ В СОХРАНЕНИИ ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ!.
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)

import requests 
from bs4 import BeautifulSoup as bs
from functools import lru_cache

class PhoneRadar:
    """Информация получаемая с сайта phoneradar.ru никак\n
    не синхронизирован/связан с noblack-mail а так-же с noblack.command.
    :param: `user_number` - Номер телефона."""
    
    def __init__(self, user_number: str) -> None:
        self.__phoneradar_url: str = "https://phoneradar.ru/phone/"
        self.__not_found_text: str = "Информация отсутствует"
        self.__user_number: str = user_number
    
    @lru_cache(maxsize=None)
    def __get_site_resurces(self):
        """Получает ресурсы сайта phoneradar.ru
        :param: `self.__phoneradar_url : str`
        :param: `self.__user_number : str`
        :return: `__resurce : bytes`"""

        try:
            __resurce: bytes = requests.get(self.__phoneradar_url + self.__user_number)
            return __resurce.content
        
        except requests.exceptions.ConnectionError as connection_error:
            return False

    @property
    def get_rating(self):
        """Определяет рейтинг номера телефона.
        :param: `__get_site_resurce : bytes`
        :return: `rating : srt - Рейтинг номера телефона`
        :return: `rating_link : srt - Ссылка на рейтинг номера телефона`"""
        
        resurce: bytes = self.__get_site_resurces()
        if resurce:
            try:
                rating_link: str = self.__phoneradar_url + self.__user_number
                response: bytes = bs(resurce, "html.parser").find("div", class_="card-body")
                rating: str = response.find("div", class_="alert").text.strip()
                print(rating_link)
                return rating, rating_link
                
            except AttributeError:
                return self.__not_found_text, rating_link
                print(rating_link)
        print(rating_link)
        return self.__not_found_text, rating_link
    
