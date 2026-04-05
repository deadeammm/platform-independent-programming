from pathlib import Path
from datetime import date

# -------------------------------------------------
# КРОССПЛАТФОРМЕННЫЙ ПУТЬ К ФАЙЛУ ДАННЫХ
# Файл journal.txt будет храниться в папке data
# рядом с программой
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

JOURNAL_FILE = DATA_DIR / "journal.txt"


def show_menu():
    """Вывод главного меню."""
    print("\n========================================")
    print("        ЖУРНАЛ НАБЛЮДЕНИЙ")
    print("========================================")
    print("1. Добавить запись")
    print("2. Показать все записи")
    print("3. Очистить журнал")
    print("4. Выход")


def input_date():
    """Ввод и проверка даты в формате YYYY-MM-DD."""
    while True:
        user_input = input("Введите дату (ГГГГ-ММ-ДД): ").strip()
        try:
            # Проверка формата и корректности даты
            parsed_date = date.fromisoformat(user_input)
            return parsed_date.isoformat()
        except ValueError:
            print("Ошибка: некорректная дата. Пример ввода: 2024-09-15")


def input_score():
    """Ввод и проверка оценки от 1 до 10."""
    while True:
        user_input = input("Введите оценку (1-10): ").strip()
        try:
            score = int(user_input)
            if 1 <= score <= 10:
                return score
            else:
                print("Ошибка: оценка должна быть в диапазоне от 1 до 10.")
        except ValueError:
            print("Ошибка: нужно ввести целое число.")


def add_record():
    """Добавление новой записи в файл."""
    print("\n--- Добавление новой записи ---")
    record_date = input_date()
    text = input("Введите текст наблюдения: ").strip()
    score = input_score()

    # Запись в формате: Дата | Оценка | Текст
    with open(JOURNAL_FILE, "a", encoding="utf-8") as file:
        file.write(f"{record_date} | {score} | {text}\n")

    print("\nЗапись успешно добавлена!")


def read_records():
    """Чтение всех записей из файла."""
    if not JOURNAL_FILE.exists():
        return []

    with open(JOURNAL_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    records = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Разделяем только на 3 части, чтобы текст мог содержать пробелы
        parts = line.split(" | ", maxsplit=2)
        if len(parts) == 3:
            record_date, score, text = parts
            records.append((record_date, score, text))

    return records


def show_records():
    """Вывод всех записей в виде таблицы и статистики."""
    records = read_records()

    print("\n--- Все записи ---")

    if not records:
        print("Журнал пуст.")
        return

    # Подготовка данных для таблицы
    date_width = 12
    score_width = 7
    text_width = 32

    # Заголовок таблицы
    border = "+" + "-" * date_width + "+" + "-" * score_width + "+" + "-" * text_width + "+"
    print(border)
    print(f"|{'Дата':^{date_width}}|{'Оценка':^{score_width}}|{'Текст':^{text_width}}|")
    print(border)

    total_score = 0

    for record_date, score, text in records:
        total_score += int(score)
        print(f"|{record_date:^{date_width}}|{score:^{score_width}}|{text[:text_width]:<{text_width}}|")

    print(border)

    # Статистика
    count = len(records)
    average_score = total_score / count

    print("\nСтатистика:")
    print(f"Всего записей: {count}")
    print(f"Средняя оценка: {average_score:.2f}")


def clear_journal():
    """Очистка журнала."""
    with open(JOURNAL_FILE, "w", encoding="utf-8") as file:
        file.write("")
    print("\nЖурнал очищен.")


def main():
    """Основной цикл программы."""
    while True:
        show_menu()
        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            clear_journal()
        elif choice == "4":
            print("\nВыход из программы.")
            break
        else:
            print("\nОшибка: выберите пункт меню от 1 до 4.")


if __name__ == "__main__":
    main()# Лабораторная работа №2
# Лабораторная работа №2
