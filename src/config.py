# -*- coding UTF-8 -*-
# NOBLACK-MAIL НИКАК НЕ УЧАСТВУЕТ В СОХРАНЕНИИ ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ!.
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)

import os


# Цветовая политра
COLOR_CODE = {
    "RESET": "\033[0m",      # Сброс цвета [Стиль]
    "UNDERLINE": "\033[04m", # Нижнее подчеркивание [Стиль]
    "GREEN": "\033[32m",     # Зеленый 
    "YELLOW": "\033[93m",    # Желтый
    "RED": "\033[31m",       # Красный
    "CYAN": "\033[36m",      # Светло голубой
    "BOLD": "\033[01m",      # Жирный [Стиль]
    "PINK": "\033[95m",      # Розовое
    "URL_L": "\033[36m",     # Ссылки [Стиль]
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m"}      # Темный

# Глоб. софт информация
GLOBAL_SOFT_INFO = {
    "AUTHOR": "FELIX4",
    "AUTHOR_LINK": "t.me/FELIX4",
    "NOLACK_AUTO_BOT": "https://t.me/noblackAuto_bot",
    "NOLACK_AUTO_SITE": "https://noblack-auto.ru",
    "SOFT_ORIGINAL_LINK": "https://github.com/DataSC3/noblack-mail.git",
    "SOFT_ORIGINAL_CHANNEL": "https://t.me/noblack_channel",
    "SOFT_VERSION": "1.0.6",
    "BLOCKED_COUNTRIES": ["Ukraine"]}


# Очистка консоли
def console_clear() -> None:
    """Очиска консоли (Windows / Linux)"""
    
    # Очистка для Windows
    if os.sys.platform == "win32": os.system("cls")

    # Очистка для Linux
    else: os.system("clear")

# Вывод лого
def print_banner() -> None:
    """Ввод баннера"""
    console_clear()
    print(F'{COLOR_CODE["RED"]}*–––––––––––––––––––––––————————*')
    print(COLOR_CODE["RED"]+ "█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █")
    print(COLOR_CODE["GREEN"] + "█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄" + COLOR_CODE["RESET"])
    print(F'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}\n* Разработчик: {COLOR_CODE["RESET"]}{COLOR_CODE["LI_G"]}{GLOBAL_SOFT_INFO["AUTHOR"]}{COLOR_CODE["RESET"]}')
    print(F'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}* Мы в Телеграме: {COLOR_CODE["RESET"]}{COLOR_CODE["LI_G"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_CHANNEL"]}{COLOR_CODE["RESET"]}')
    print(F'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}* Орегинальная ссылка: {COLOR_CODE["RESET"]}{COLOR_CODE["LI_G"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}{COLOR_CODE["RESET"]}')
    print(F'{COLOR_CODE["LI_G"]}*––––––––––––––––––—————* V {GLOBAL_SOFT_INFO["SOFT_VERSION"]}{COLOR_CODE["RESET"]} *—BETA————*\n')

# Показ текст соглашения
def print_welcome_text() -> None:
    """Вывод текст о соглашении"""
    try:
        console_clear()
        agreement_file_name: str = "src/.Соглашение"
        with open(agreement_file_name, encoding="UTF-8") as file:

            print(F'{COLOR_CODE["RED"]}*–––––––––––––––––––––––————————*')
            print(F'{COLOR_CODE["LI_G"]}{file.read()}')
            print(F'{COLOR_CODE["RED"]}*–––––––––––––––––––––––————————*')


            try: os.remove(agreement_file_name)
            except PermissionError: 
                print(F'{COLOR_CODE["RED"]}[!] К сожалению, не получилось удалить файл, содержащий пользовательское соглашение. {COLOR_CODE["LI_G"]}Этот баннер будет появляться при каждом запуске.')
                
            input(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
                f'Чтобы принять соглашение, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}ENTER ')        
    
    except FileNotFoundError: ...
    except KeyboardInterrupt:
        print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')
