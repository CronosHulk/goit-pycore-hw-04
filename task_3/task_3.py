# Завдання 3

# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії,
#  виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.



# Вимоги до завдання:

# Створіть віртуальне оточення Python для ізоляції залежностей проекту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, 
# використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

# Рекомендації для виконання:

# Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.
# Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
# Для роботи з файловою системою використовуйте модуль pathlib.
# Забезпечте належне форматування виводу, використовуючи функції colorama.

# Критерії оцінювання:

# Створення та використання віртуального оточення.
# Правильність отримання та обробки шляху до директорії.
# Точність виведення структури директорії.
# Коректне застосування кольорового виведення за допомогою colorama.
# Якість коду, включаючи читабельність, структурування та коментарі.

# Приклад використання:

# Якщо виконати скрипт та передати йому абсолютний шлях до директорії як параметр.

# python hw03.py /шлях/до/вашої/директорії

# Це призведе до виведення в терміналі списку всіх піддиректорій та файлів у вказаній директорії з використанням різних кольорів 
# для піддиректорій та файлів, що полегшить візуальне сприйняття файлової структури.

# Для директорії зі наступною структурою

# 📦picture
#  ┣ 📂Logo
#  ┃ ┣ 📜IBM+Logo.png
#  ┃ ┣ 📜ibm.svg
#  ┃ ┗ 📜logo-tm.png
#  ┣ 📜bot-icon.png
#  ┗ 📜mongodb.jpg

# Скрипт повинен вивести схожу структуру

import sys
import os
from pathlib import Path
from colorama import Fore, Style
from typing import List

COLOR_DIR = Fore.BLUE + Style.BRIGHT
COLOR_FILE = Fore.GREEN              
COLOR_RESET = Style.RESET_ALL

ELBOW = "└──"
TEE = "├──"
PIPE = "│  "
SPACE = "   "

def display_tree(root_path=Path, prefix='', is_root=True):
    if is_root:
        root_name = root_path.name if root_path.name else root_path.resolve().name
        print(f"{COLOR_DIR}# 📦{root_name}{COLOR_RESET}")

    try:
        entries = sorted(list(root_path.iterdir()))
    except Exception as e:
        print(f"{prefix} ❌ {Fore.RED}Помилка доступу до {root_path.name}: {e}{COLOR_RESET}")
        return

    items_count = len(entries)

    for i, entry in enumerate(entries):
        is_last = (i == items_count - 1)

        connector = ELBOW if is_last else TEE

        if entry.is_dir():
            color_line = f"{COLOR_DIR}{connector} 📂{entry.name}{COLOR_RESET}"
            print(prefix + color_line)

            next_prefix = prefix + (SPACE if is_last else PIPE)

            display_tree(entry, next_prefix, is_root=False)
        else:
            color_line = f"{COLOR_FILE}{connector} 📜{entry.name}{COLOR_RESET}"
            print(prefix + color_line)

def visualize_directory_structure():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Необхідно вказати шлях до директорії як аргумент.")
        print(f"Використання: python3 {os.path.basename(sys.argv[0])} <шлях/до/директорії>{COLOR_RESET}")
        sys.exit(1)

    path_arg = sys.argv[1]
    target_path = Path(path_arg)

    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path_arg}' не існує.{COLOR_RESET}")
        sys.exit(1)

    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{path_arg}' не є директорією.{COLOR_RESET}")
        sys.exit(1)

    print("--- Структура директорії ---")
    display_tree(target_path)
    print("----------------------------")


visualize_directory_structure()
