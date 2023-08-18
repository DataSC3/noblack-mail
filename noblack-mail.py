# -*- coding UTF-8 -*-
# КОММАНДА: noblack.command
# НОВОСТИ: t.me/noblack_channel
# АВТОР: FELIX4
# DATE: Вторник, 18 Апреля 2023 г. 03:39:15 (+03)


try:
    # Проверка на наличие модулей
    from src.config import COLOR_CODE, GLOBAL_SOFT_INFO, print_banner, print_welcome_text
    from src.httpweb_ip import HttpWebIp
    from src.httpweb_mnp import HttpWebMnp
    from src.httpweb_number import HttpWebNumber
    from src.blocked_countries import BlockedCountries
    from src.update.update import Update
    from src.noblack_auto import print_noblack_auto_text
    from time import sleep
    import requests, bs4


except ImportError:
    # Совет по установке модулей и выход
    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] {COLOR_CODE["DARK"]}ВНИМАНИЕ У ВАС ПРОБЛЕМКА, НО МЫ ЕГО РЕШИМ!{COLOR_CODE["RESET"]}')

    print(f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}Оригинально программное обеспечение находиться на: '+
         f'{COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}{COLOR_CODE["RESET"]}\n'+
         f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}'+
         f'Мы в телеграмме: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_CHANNEL"]}{COLOR_CODE["RESET"]}')
    
    exit(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}У вас отсутствует модули: '+
         f'{COLOR_CODE["CYAN"]}requests{COLOR_CODE["RESET"]} и/или {COLOR_CODE["CYAN"]}'+
         f'bs4{COLOR_CODE["RESET"]}. {COLOR_CODE["RED"]}\n[*] {COLOR_CODE["YELLOW"]}'+
         f'Напишите в терминал/консоль: {COLOR_CODE["GREEN"]}apt-get install python3-pip && pip3 install requests bs4{COLOR_CODE["RESET"]}')


if __name__ == "__main__":
    # Показ текст соглашении
    print_welcome_text()

    while True:
        # Показ баннера
        print_banner()

        # Меню управления
        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[1] {COLOR_CODE["LI_G"]}'
            f'Проверить {COLOR_CODE["RED"]}Номер{COLOR_CODE["LI_G"]} телефона.{COLOR_CODE["RESET"]}\n'
            
            f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[2] {COLOR_CODE["LI_G"]}'
            f'Проверить {COLOR_CODE["RED"]}MNP{COLOR_CODE["LI_G"]} телефона.{COLOR_CODE["RESET"]}\n'
            
            f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[3] {COLOR_CODE["LI_G"]}'
            f'Проверить {COLOR_CODE["RED"]}IP{COLOR_CODE["LI_G"]} телефона.{COLOR_CODE["RESET"]}\n'

            f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[4] {COLOR_CODE["LI_G"]}'
            f'Проверить {COLOR_CODE["RED"]}Гос. номер{COLOR_CODE["LI_G"]} автомобиля.{COLOR_CODE["RESET"]}\n'
            
            f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[5] {COLOR_CODE["LI_G"]}'
            f'Провести техническую проверку {COLOR_CODE["RED"]}на работоспосбность сервиса.{COLOR_CODE["LI_G"]}{COLOR_CODE["RESET"]}\n')

        try:
        
            # Выбор варианта поиска
            user_chooice: str = input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[–] {COLOR_CODE["LI_G"]}'
                f'Выберите вариант поиска: {COLOR_CODE["RESET"]}').strip()
            
            # Поиск по номеру телефона
            if not user_chooice or user_chooice == "1":
                httpweb_number = HttpWebNumber()
                httpweb_number.print_number_results
                sleep(3)

            # Поиск MNP по номеру телефона
            elif user_chooice == "2":
                httpweb_number = HttpWebMnp()
                httpweb_number.print_mnp_results
                sleep(3)

            # Поиск по IP
            elif user_chooice == "3":
                httpweb_number = HttpWebIp()
                httpweb_number.print_ip_results
                sleep(3)

            # Поиск по Гос. номеру
            elif user_chooice == "4":
                print_noblack_auto_text()

            # Проверка тех. части
            elif user_chooice == "5":
                # Проверка на блокировку
                BlockedCountries().print_ip_result()
                
                # Проверка обновлении
                Update().get()
                
                input(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
                  f'Чтобы вернуться назад, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}ENTER ')

            # Повторный опрос
            else: continue

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')
            break
