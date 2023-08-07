# -*- coding UTF-8 -*-
# NOBLACK-MAIL НИКАК НЕ УЧАСТВУЕТ В СОХРАНЕНИИ ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ!.
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)

import requests
from time import sleep
from .config import COLOR_CODE, console_clear, GLOBAL_SOFT_INFO

class BlockedCountries:
    """Проверка пользовательского IP в наличии заблокированных стран"""

    def __init__(self) -> None:
        self.__my_ip: str = "https://api.myip.com"
        self.__country: list = GLOBAL_SOFT_INFO["BLOCKED_COUNTRIES"]

    @property
    def __get_ip_result(self):
        """Получение данных об IP клиента
        :param self.__my_ip: Ссылка на получение IP клиента;
        :return __my_ip_result: Результат"""

        # Получение данных
        try: __my_ip_result: dict = requests.get(self.__my_ip, timeout=6).json()
        except: __my_ip_result: dict = {"status_error": True}
        return __my_ip_result

    def print_ip_result(self) -> None:
        """Показ результатов IP теста на блокировку
        :param self.__get_ip_result: Получение данных об IP;
        :return None: Результат"""
        
        # Очистка консоли 
        console_clear()

        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[%] {COLOR_CODE["LI_G"]}'
        f'Производиться проверка технической части..{COLOR_CODE["RESET"]}')
        sleep(2)
        
        ip_data = self.__get_ip_result
        ip_county = ip_data.get("country")

        # Если страна имееться в списке заблокированных стран
        if ip_county in self.__country:
            print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] '+
                  f'{COLOR_CODE["RED"]}К сожалению, наш сервис недоступен в вашей стране {COLOR_CODE["RESET"]}({ip_county}){COLOR_CODE["DARK"]}, воспользуйтесь VPN`ом для получении доступа к ресурсам.')
            
            sleep(1.7)

        # Отстутствует интеренет соединение
        if ip_data.get("status_error"):
            print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] '+
                  f'{COLOR_CODE["RED"]}К сожалению, у вас {COLOR_CODE["RESET"]}отсутствует {COLOR_CODE["RED"]}интернет соединение')
            
            sleep(1.7)

        else:
            print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[*] {COLOR_CODE["LI_G"]}'
                f'Проверка технической части для страны {COLOR_CODE["RESET"]}"{ip_county}"{COLOR_CODE["LI_G"]}, прошла успешно!')
        
            sleep(1.7)
        
        
            
