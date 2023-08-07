# -*- coding UTF-8 -*-
# КОММАНДА: noblack.command
# НОВОСТИ: t.me/noblack_channel
# АВТОР: FELIX4
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)


try:
    # Проверка на наличие модулей
    from src.config import COLOR_CODE, GLOBAL_SOFT_INFO, console_clear, print_banner, print_welcome_text
    from src.httpweb_ip import HttpWebIp
    from src.httpweb_mnp import HttpWebMnp
    from src.httpweb_number import HttpWebNumber
    from src.noblack_auto import print_noblack_auto_text
    import requests
    import bs4 
    import os

except ImportError:
    # Совет по установке модулей и выход
    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] {COLOR_CODE["DARK"]}ВНИМАНИЕ У ВАС ПРОБЛЕМКА, НО МЫ ЕГО РЕШИМ!{COLOR_CODE["RESET"]}')

    print(f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}Оригинальное программное обеспечение находиться на: '+
         f'{COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}{COLOR_CODE["RESET"]}\n'+
         f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}'+
         f'Мы в телеграмме: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_CHANNEL"]}{COLOR_CODE["RESET"]}')
    
    exit(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}У вас отсутствует модули: '+
         f'{COLOR_CODE["CYAN"]}requests{COLOR_CODE["RESET"]} и/или {COLOR_CODE["CYAN"]}'+
         f'bs4{COLOR_CODE["RESET"]}. {COLOR_CODE["RED"]}\n[*] {COLOR_CODE["YELLOW"]}'+
         f'Напишите в терминал/консоль: {COLOR_CODE["GREEN"]}pip3 install requests bs4{COLOR_CODE["RESET"]}')


if __name__ == "__main__":
    # Показ текст соглашении
    print_welcome_text()

    # Показ баннера
    print_banner()

    # Меню управления
    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[1] {COLOR_CODE["LI_G"]}'
        f'Проверить {COLOR_CODE["RED"]}номер{COLOR_CODE["LI_G"]} телефона {COLOR_CODE["RESET"]}\n'
        
        f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[2] {COLOR_CODE["LI_G"]}'
        f'Проверить {COLOR_CODE["RED"]}MNP{COLOR_CODE["LI_G"]} телефона {COLOR_CODE["RESET"]}\n'
        
        f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[3] {COLOR_CODE["LI_G"]}'
        f'Проверить {COLOR_CODE["RED"]}IP{COLOR_CODE["LI_G"]} телефона {COLOR_CODE["RESET"]}\n'

        f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[4] {COLOR_CODE["LI_G"]}'
        f'Проверить {COLOR_CODE["RED"]}Гос. номер{COLOR_CODE["LI_G"]} автомобиля{COLOR_CODE["RESET"]}\n')


    try:
        # Выбор варианта поиска
        user_chooice: str = input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[–] {COLOR_CODE["LI_G"]}'
            f'Выберите вариант поиска: {COLOR_CODE["RESET"]}').strip()
        
        # Поиск по номеру телефона
        if not user_chooice or user_chooice == "1":
            httpweb_number = HttpWebNumber()
            httpweb_number.print_number_results

        # Поиск MNP по номеру телефона
        if user_chooice == "2":
            httpweb_number = HttpWebMnp()
            httpweb_number.print_mnp_results

        # Поиск по IP
        if user_chooice == "3":
            httpweb_number = HttpWebIp()
            httpweb_number.print_ip_results

        if user_chooice == "4":
            print_noblack_auto_text()


    except KeyboardInterrupt:
        print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')
