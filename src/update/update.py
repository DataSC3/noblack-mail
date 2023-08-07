# -*- coding UTF-8 -*-
# ИНФОРМАЦИЯ БЫЛА ПОЛУЧЕНА ОТ HTMLWEB.RU
# NOBLACK-MAIL НИКАК НЕ УЧАСТВУЕТ В СОХРАНЕНИИ ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ!.
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)

import requests
from ..config import GLOBAL_SOFT_INFO, COLOR_CODE
from bs4 import BeautifulSoup as bs


class Update:
    def __init__(self) -> None:
        self.__update_link: str = F'{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"][:-4]}/commits/main'

    def __str__(self) -> str:
        return F"Description: Обновляет клиент и/или уведомляет о новой версии: {self.__update_link}"

    def __repr__(self) -> str:
        return (F"Description: Обновляет клиент и/или уведомляет о новой версии: {self.__update_link}\n" +
                F"Modules: requests, bs4\n" +
                F"GITHUB/COMMITS/MAIN")
    @property
    def check(self) -> int:
        """Получение кол-во коммитов
        :param self.__update_link: Ссылка на репозиторий
        :return bs_content_len: Кол-во коммитов"""

        try:
            # Проверка обновлении по ссылке
            github_commits_content = requests.get(url=self.__update_link)
            if github_commits_content.status_code != 200:
                print(f'{COLOR_CODE["RED"]}[!] Ошибка, не получилось проверить наличие обновлении! {COLOR_CODE["RESET"]}\n')    

            else:
                bs_content_len: int = len(bs(github_commits_content.text, "html.parser")
                .find("div", class_="container-xl")
                .find_all("li"))
                
                return bs_content_len        
        
        except requests.exceptions.ConnectionError as connection_error:
            print(f'{COLOR_CODE["RED"]}[!] Ошибка, не получилось проверить наличие обновлении! {COLOR_CODE["RESET"]}')
            return None
        
        except Exception as error: 
            print(f'{COLOR_CODE["RED"]}[!] Информация об ошибке: {COLOR_CODE["RESET"]}')
            print(f'{COLOR_CODE["DARK"]}{error}{COLOR_CODE["RESET"]}\n')
            return None
    
    def get(self):
        """Получение обновлений и обновление"""
        
        try:
            version_file_name: str = "src/update/version"
            with open(file=version_file_name, mode="r") as file_read:
                now_version = int(file_read.read().strip())

                # Проверка на полученние новой версии и сравнение версии
                if self.check and type(self.check) == int and now_version != self.check:
                    
                    print(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[^] {COLOR_CODE["LI_G"]}'
                    f'Доступно новое {COLOR_CODE["RED"]}обновление!!.{COLOR_CODE["RESET"]}')
                    
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[?] {COLOR_CODE["LI_G"]}'
                        f'Чтобы обновить, {COLOR_CODE["RED"]}удалите эту версию {COLOR_CODE["LI_G"]}и установите новую по исходной ссылке:{COLOR_CODE["CYAN"]}') 
                    
                    print(F'[*] {COLOR_CODE["LI_G"]}Ссылка: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}')
                    
                    # Запись новых данных в файл версии
                    with open(file=version_file_name, mode="w") as file_write: 
                        file_write.write(str(self.check))

                # Новой версии еще нет
                else:
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[*] {COLOR_CODE["LI_G"]}'
                    f'Новые обновлении еще не доступны.{COLOR_CODE["RESET"]}')
        


        except FileNotFoundError: ...
        except ValueError:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Поврежден файл "version"{COLOR_CODE["RESET"]} (noblack-mail/src/update/version)')
            print(f'{COLOR_CODE["RED"]}[*] {COLOR_CODE["YELLOW"]}Проверка наличия обновлений, недоступно.{COLOR_CODE["RESET"]} Переустановите софт.')
            print(F'{COLOR_CODE["RED"]}[*] {COLOR_CODE["YELLOW"]}Ссылка: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}')

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')
