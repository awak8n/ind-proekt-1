"""
Система обработки предложений пользователей.

Начальный сценарий (ПР1):
консольная регистрация предложений, расчёт приоритета,
просмотр и рассмотрение предложений.
"""

from datetime import date


def get_review_status(is_reviewed):
    """Возвращает текстовый статус рассмотрения предложения."""
    if is_reviewed:
        return "Предложение рассмотрено"
    else:
        return "Предложение ожидает рассмотрения"


def calculate_priority(votes, category):
    """Определяет приоритет предложения по числу голосов и категории."""
    if votes >= 50:
        priority = "Высокий"
    elif votes >= 20:
        priority = "Средний"
    else:
        priority = "Низкий"

    # Предложения по безопасности всегда получают высокий приоритет
    if category == "Безопасность":
        priority = "Высокий"

    return priority


def make_decision(is_reviewed, priority):
    """Выносит решение по предложению после рассмотрения."""
    if not is_reviewed:
        return "Решение не вынесено"

    if priority == "Высокий":
        return "Принято"
    elif priority == "Средний":
        return "Принято с доработкой"
    else:
        return "Отклонено"


def format_summary(title, category, votes, priority, status):
    """Формирует краткую сводку по предложению."""
    return (
        f"«{title}» | Категория: {category} | "
        f"Голоса: {votes} | Приоритет: {priority} | Статус: {status}"
    )


def add_suggestion(suggestions):
    """Добавляет новое предложение через консоль."""

    print("\n--- ДОБАВЛЕНИЕ ПРЕДЛОЖЕНИЯ ---")

    title = input("Название предложения: ").strip()

    while not title:
        print("Название не может быть пустым.")
        title = input("Название предложения: ").strip()

    print("\nВыберите категорию:")
    print("1. UI/UX")
    print("2. Функциональность")
    print("3. Безопасность")

    category_choice = input("Ваш выбор: ").strip()

    categories = {
        "1": "UI/UX",
        "2": "Функциональность",
        "3": "Безопасность"
    }

    while category_choice not in categories:
        print("Ошибка. Выберите 1, 2 или 3.")
        category_choice = input("Ваш выбор: ").strip()

    category = categories[category_choice]

    votes_str = input("Количество голосов: ").strip()

    while not votes_str.isdigit():
        print("Ошибка. Введите целое число.")
        votes_str = input("Количество голосов: ").strip()

    votes = int(votes_str)

    author_email = input("Email автора: ").strip()

    while not author_email:
        print("Email не может быть пустым.")
        author_email = input("Email автора: ").strip()

    suggestion = {
        "title": title,
        "category": category,
        "votes": votes,
        "is_reviewed": False,
        "submission_date": date.today(),
        "author_email": author_email
    }

    suggestions.append(suggestion)

    priority = calculate_priority(votes, category)
    status = get_review_status(False)

    print("\n✓ Предложение успешно добавлено!")
    print(f"Дата подачи: {suggestion['submission_date']}")
    print(f"Автор: {author_email}")
    print(format_summary(
        title,
        category,
        votes,
        priority,
        status
    ))


def show_suggestions(suggestions):
    """Показывает все зарегистрированные предложения."""

    print("\n--- СПИСОК ПРЕДЛОЖЕНИЙ ---")

    if not suggestions:
        print("Предложений пока нет.")
        return

    for number, suggestion in enumerate(suggestions, start=1):

        priority = calculate_priority(
            suggestion["votes"],
            suggestion["category"]
        )

        status = get_review_status(
            suggestion["is_reviewed"]
        )

        decision = make_decision(
            suggestion["is_reviewed"],
            priority
        )

        print(f"\nПредложение №{number}")
        print(f"Дата подачи: {suggestion['submission_date']}")
        print(f"Автор: {suggestion['author_email']}")

        print(format_summary(
            suggestion["title"],
            suggestion["category"],
            suggestion["votes"],
            priority,
            status
        ))

        print(f"Решение: {decision}")


def review_suggestion(suggestions):
    """Рассматривает выбранное предложение."""

    print("\n--- РАССМОТРЕНИЕ ПРЕДЛОЖЕНИЯ ---")

    if not suggestions:
        print("Предложений пока нет.")
        return

    for number, suggestion in enumerate(suggestions, start=1):
        print(
            f"{number}. {suggestion['title']} "
            f"({suggestion['category']})"
        )

    choice = input("\nВведите номер предложения: ").strip()

    while (
        not choice.isdigit()
        or not (1 <= int(choice) <= len(suggestions))
    ):
        print("Ошибка. Такого номера нет.")
        choice = input("Введите номер предложения: ").strip()

    index = int(choice) - 1
    suggestion = suggestions[index]

    priority = calculate_priority(
        suggestion["votes"],
        suggestion["category"]
    )

    suggestion["is_reviewed"] = True

    decision = make_decision(
        True,
        priority
    )

    print("\n✓ Предложение рассмотрено!")
    print(f"Название: {suggestion['title']}")
    print(f"Приоритет: {priority}")
    print("Статус: Предложение рассмотрено")
    print(f"Решение: {decision}")


def show_menu():
    """Выводит главное меню программы."""

    print("\n")
    print("=" * 50)
    print(" СИСТЕМА ОБРАБОТКИ ПРЕДЛОЖЕНИЙ ПОЛЬЗОВАТЕЛЕЙ")
    print("=" * 50)
    print("1. Добавить предложение")
    print("2. Показать предложения")
    print("3. Рассмотреть предложение")
    print("4. Выйти")
    print("=" * 50)


def main():
    """Главная функция консольного приложения."""

    suggestions = []

    print("\nДобро пожаловать в систему обработки предложений!")

    while True:

        show_menu()

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            add_suggestion(suggestions)

        elif choice == "2":
            show_suggestions(suggestions)

        elif choice == "3":
            review_suggestion(suggestions)

        elif choice == "4":
            print("\nПрограмма завершена.")
            break

        else:
            print("\nОшибка: выберите пункт от 1 до 4.")


if __name__ == "__main__":
    main()