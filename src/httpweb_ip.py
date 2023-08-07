# -*- coding UTF-8 -*-
# ИНФОРМАЦИЯ БЫЛА ПОЛУЧЕНА ОТ HTMLWEB.RU
# NOBLACK-MAIL НИКАК НЕ УЧАСТВУЕТ В СОХРАНЕНИИ ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ!.
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)

import requests
from .config import COLOR_CODE, console_clear
from functools import lru_cache

# Проверка по IP
class HttpWebIp:
    """Информация получаемая с сайта httpweb.ru и httpbin.ru никак\n
    не синхронизирован/связан с noblack-mail а так-же с noblack.command.
    :param: `user_number` - Номер телефона."""


    def __init__(self) -> None:
        self.__my_ip_link: str = "https://httpbin.org/ip"
        self.__check_ip_link: str = "https://htmlweb.ru/geo/api.php?json&ip="
        self.__not_found_text: str = "Информация отсутствует"

    # Получение IP пользователя
    @lru_cache(maxsize=None)
    def __return_user_ip(self) -> str:
        """Получение IP пользователя\n
        IP Адрес пользователя получают после разрешения самого пользователя.
        
        :param: `self.__my_ip_link:` str — Адрес сайта для получения IP клиента.
        :return: `return_user_ip:` str - IP клиента.
        """

        # Получение IP пользователя 
        try:
            __my_ip = requests.get(self.__my_ip_link)
        
            if __my_ip.ok:
                __return_user_ip: str = __my_ip.json().get("origin", "Ошибка при получении IP")
            
            else:
                __return_user_ip: str = "Ошибка при получении IP"

        except requests.exceptions.ConnectionError as connection_error:
            __return_user_ip: str = "Ошибка при получении IP"

        # Результат поиска
        return __return_user_ip

    # Получение данных по IP
    @lru_cache(maxsize=None)
    def __return_ip_data(self, user_ip: str) -> dict:
        """Получение данных по поисковому IP
        param: `self.__check_ip_link:` str — Адрес сайта для получения данных по чужому IP.
        return: `__return_ip_data:` dict - Данные IP искомого.
        """

        # Получение данных IP искомого  
        try:
            __result_ip_data = requests.get(self.__check_ip_link + user_ip)
        
            if __result_ip_data.ok:
                __return_ip_data: dict = __result_ip_data.json()
            
            else:
                __return_ip_data: dict = {"status_error": True}

        except requests.exceptions.ConnectionError as connection_error:
            __return_ip_data: dict = {"status_error": True}
        
        return __return_ip_data

    # Ввод данных в консоль
    @property
    def print_ip_results(self) -> str:
        """Вывод полученных данных"""
        try:
            
            # Получение разрешении на просмотр IP пользователя
            console_clear()
            _user_permission = str = input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}?{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
                f'Разрешите увидеть ваш IP {COLOR_CODE["DARK"]}(Да - 1 / Нет - 0): {COLOR_CODE["RESET"]}').strip()
            
            if not _user_permission or _user_permission == "1":
                _my_ip = self.__return_user_ip()
                _user_permission = True
            
            else:
                _my_ip = self.__not_found_text
            # -----------------------------------------------
            
            print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[#] {COLOR_CODE["LI_G"]}Ваш IP:' +
                f' {COLOR_CODE["DARK"]}{_my_ip}{COLOR_CODE["RESET"]}')
            
            _user_ip: str = input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[*] {COLOR_CODE["LI_G"]}' + 
                f'Введите IP: {COLOR_CODE["RESET"]}').strip()
            
            # Если ввели IP
            if _user_ip:
                print(f'{COLOR_CODE["RED"]}[~] {COLOR_CODE["YELLOW"]}Поиск данных.. {COLOR_CODE["RESET"]}\n')
                _get_user_ip_data = self.__return_ip_data(user_ip=_user_ip)

                # Проверка статуса ошибки
                if _get_user_ip_data.get("limit") <= 0:
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] '+
                        f'{COLOR_CODE["RESET"]}К сожалению, вы израсходовали {COLOR_CODE["DARK"]}все лимиты')
                    
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["RESET"]}Всего лимитов: {COLOR_CODE["DARK"]}'+
                        f'{_get_user_ip_data.get("limit", self.__not_found_text)}{COLOR_CODE["RESET"]}')
                
                # Проверка статуса ошибки
                elif _get_user_ip_data.get("status_error") or _get_user_ip_data.get("error"):
                    print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Данные не найдены {COLOR_CODE["RESET"]}\n')

                # Ввод IP данных
                else:
                    _ip_data_country = _get_user_ip_data.get('country')
                    _ip_data_region = _get_user_ip_data.get('region')
                    
                    # Страна
                    # Для украины информация о стране отсутствует
                    if _ip_data_country.get("country_code3") == 'UKR':
                        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                            f'{COLOR_CODE["LI_G"]}Страна:{COLOR_CODE["F_CL"]} Украина{COLOR_CODE["RESET"]}')
                    
                    else:
                        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                            f'{COLOR_CODE["LI_G"]}Страна:{COLOR_CODE["F_CL"]} '+
                            f'{_ip_data_country.get("name", self.__not_found_text)}, {_ip_data_country.get("fullname", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Код страны
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Код страны:{COLOR_CODE["F_CL"]} '+
                        f'{_ip_data_country.get("country_code3", self.__not_found_text)}{COLOR_CODE["RESET"]}')
                    
                    # Код номеров телефона
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Код номеров:{COLOR_CODE["F_CL"]} '+
                        f'{_ip_data_country.get("telcod", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Локация
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Локация:{COLOR_CODE["F_CL"]} '+
                        f'{_ip_data_country.get("location", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Разговорный речь (Язык)
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Язык:{COLOR_CODE["F_CL"]} '+
                        f'{_ip_data_country.get("lang", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Город (Где используеться номер телефона)
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Город:{COLOR_CODE["F_CL"]} '+
                        f'{_ip_data_region.get("name", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Код машин города
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Код машин:{COLOR_CODE["F_CL"]} '+
                        f'{_get_user_ip_data.get("autocod", self.__not_found_text)}{COLOR_CODE["RESET"]}')
                    
                    # Широта
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Широта:{COLOR_CODE["F_CL"]} '+
                        f'{_get_user_ip_data.get("latitude", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Долгота
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["LI_G"]}Долгота:{COLOR_CODE["F_CL"]} '+
                        f'{_get_user_ip_data.get("longitude", self.__not_found_text)}{COLOR_CODE["RESET"]}')
                    
                    # Всего лимитов
                    print(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["RED"]}Всего лимитов: '+
                        f'{_get_user_ip_data.get("limit", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
                        f'Чтобы завершить поиск, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}ENTER ')
            
            # Если не ввели IP
            else:
                print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Ошибка, введите IP! {COLOR_CODE["RESET"]}\n')

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')

