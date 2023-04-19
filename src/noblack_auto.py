# -*- coding UTF-8 -*-
# ИНФОРМАЦИЯ БУДЕТ ПРЕДОСТАВЛЕНА ДОЧЕРНЕМУ ПРОЕКТУ NOBLACK-AUTO.RU
# NOBLACK-MAIL НИКАК НЕ УЧАСТВУЕТ В СОХРАНЕНИИ ПОЛЬЗОВАТЕЛЬСКИХ ДАННЫХ!.
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)

from .config import COLOR_CODE, GLOBAL_SOFT_INFO, console_clear


def print_noblack_auto_text():
    """Показ вспомогательных данных"""
    try:
        console_clear()
        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}*{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}'
            f'Для проверки автомобилей (Сайт):{COLOR_CODE["RESET"]} {GLOBAL_SOFT_INFO["NOLACK_AUTO_SITE"]}')

        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}*{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}'
            f'Для проверки автомобилей (Телеграмм):{COLOR_CODE["RESET"]} {GLOBAL_SOFT_INFO["NOLACK_AUTO_BOT"]}')

        input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
            f'Чтобы завершить поиск, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}ENTER ')

    except KeyboardInterrupt:
        print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')
