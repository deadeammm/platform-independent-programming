from pathlib import Path
from datetime import datetime
import json

# -------------------------------------------------
# Кроссплатформенный путь к JSON-файлу
# Файл notes.json будет храниться в папке data
# рядом с программой
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

NOTES_FILE = DATA_DIR / "notes.json"


def load_notes():
    """Загрузка заметок из JSON-файла."""
    if not NOTES_FILE.exists():
        return []

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_notes(notes):
    """Сохранение списка заметок в JSON-файл."""
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)


def show_menu():
    """Вывод главного меню."""
    print("\n========================================")
    print("          ДНЕВНИК ЗАМЕТОК")
    print("========================================")
    print("1. Создать новую заметку")
    print("2. Показать все заметки")
    print("3. Найти заметку по дате")
    print("4. Выход")


def create_note():
    """Создание новой заметки."""
    print("\n--- Создание новой заметки ---")
    title = input("Введите заголовок заметки: ").strip()
    text = input("Введите текст заметки: ").strip()

    # Получение текущих даты и времени
    now = datetime.now()

    # Формирование словаря заметки
    note = {
        "title": title,
        "text": text,
        "datetime": now.isoformat()
    }

    notes = load_notes()
    notes.append(note)
    save_notes(notes)

    print("\nЗаметка успешно сохранена!")


def format_note(note, index=None):
    """Красивое форматирование одной заметки для вывода."""
    note_datetime = datetime.fromisoformat(note["datetime"])
    date_str = note_datetime.strftime("%d.%m.%Y")
    time_str = note_datetime.strftime("%H:%M:%S")

    prefix = f"{index}. " if index is not None else ""
    return (
        f"{prefix}Заголовок: {note['title']}\n"
        f"   Текст: {note['text']}\n"
        f"   Дата и время: {date_str} {time_str}\n"
    )


def show_all_notes():
    """Вывод всех заметок."""
    notes = load_notes()

    print("\n--- Все заметки ---")

    if not notes:
        print("Заметок пока нет.")
        return

    for i, note in enumerate(notes, start=1):
        print(format_note(note, i))
        print("-" * 40)

    print(f"Количество заметок: {len(notes)}")


def find_notes_by_date():
    """Поиск заметок по дате."""
    notes = load_notes()

    if not notes:
        print("\nЗаметок пока нет.")
        return

    user_date = input("Введите дату (ДД.ММ.ГГГГ): ").strip()

    try:
        target_date = datetime.strptime(user_date, "%d.%m.%Y").date()
    except ValueError:
        print("Ошибка: неверный формат даты. Пример: 15.09.2024")
        return

    found_notes = []
    for note in notes:
        note_date = datetime.fromisoformat(note["datetime"]).date()
        if note_date == target_date:
            found_notes.append(note)

    print("\n--- Результат поиска ---")

    if not found_notes:
        print("Заметки за эту дату не найдены.")
        return

    for i, note in enumerate(found_notes, start=1):
        print(format_note(note, i))
        print("-" * 40)

    print(f"Найдено заметок: {len(found_notes)}")


def main():
    """Основной цикл программы."""
    while True:
        show_menu()
        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            create_note()
        elif choice == "2":
            show_all_notes()
        elif choice == "3":
            find_notes_by_date()
        elif choice == "4":
            print("\nВыход из программы.")
            break
        else:
            print("\nОшибка: выберите пункт меню от 1 до 4.")


if __name__ == "__main__":
    main()