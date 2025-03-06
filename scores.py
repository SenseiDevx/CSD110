def valid_score(score):
    try:
        score = int(score)
        return 0 <= score <= 100
    except ValueError:
        return False


def processing_scores(filename):
    total_score = 0
    count = 0
    min_score = 100
    max_score = 0

    try:
        with open(filename, "r") as file:
            while True:
                name = file.readline().strip()
                if not name:
                    break

                score = file.readline().strip()
                if not score:
                    continue

                if score.startswith("Minimum score is") or score.startswith("Maximum score is") or score.startswith("Average is"):
                    continue

                if valid_score(score):
                    score = int(score)
                    total_score += score
                    count += 1

                    if score < min_score:
                        min_score = score
                    if score > max_score:
                        max_score = score

        if count == 0:
            print("No valid grades on file.")
            return None, None, None

        average_score = total_score / count

        with open(filename, "a") as file:
            file.write(f"Minimum score is {min_score}\n")
            file.write(f"Maximum score is {max_score}\n")
            file.write(f"Average is {average_score}\n")

        return min_score, max_score, average_score

    except FileNotFoundError:
        print("Error: File not found")
        return None, None, None


def main():
    filename = "scores.txt"
    min_score, max_score, average_score = processing_scores(filename)

    if min_score is None:
        return

    student_name = input("Whose score would you like to retrieve? --> ").strip()

    with open(filename, "r") as file:
        found = False
        while True:
            name = file.readline().strip()
            if not name:
                break

            score = file.readline().strip()
            if valid_score(score) and name == student_name:
                print(f"{student_name}'s score is {score}")
                found = True
                break

    if not found:
        print(f"{student_name} did not have a valid score")

    print(f"Minimum score is {min_score}")
    print(f"Maximum score is {max_score}")
    print(f"Average is {average_score}")


if __name__ == "__main__":
    main()


# # Функция для проверки, является ли оценка числом от 0 до 100
# def is_valid_score(score):
#     try:
#         # Пробуем преобразовать строку в число
#         score = int(score)
#         # Проверяем, находится ли оно в допустимом диапазоне
#         return 0 <= score <= 100
#     except ValueError:
#         # Если произошла ошибка (например, строка "BogusScore"), возвращаем False
#         return False
#
# # Функция для обработки файла с оценками
# def process_scores(filename):
#     total_score = 0  # Переменная для суммы всех оценок
#     count = 0  # Количество валидных оценок
#     min_score = 100  # Минимальная оценка (начинаем с 100, чтобы потом уменьшать)
#     max_score = 0  # Максимальная оценка (начинаем с 0, чтобы потом увеличивать)
#
#     try:
#         # Открываем файл для чтения
#         with open(filename, "r") as file:
#             while True:
#                 name = file.readline().strip()  # Читаем имя студента
#                 if not name:  # Если имя пустое, значит конец файла
#                     break
#
#                 score = file.readline().strip()  # Читаем оценку
#                 if not score:  # Если строки нет, пропускаем
#                     continue
#
#                 # Пропускаем старые записи с min/max/avg
#                 if score.startswith("Minimum score is") or score.startswith("Maximum score is") or score.startswith("Average is"):
#                     continue
#
#                 # Проверяем, валидная ли оценка
#                 if is_valid_score(score):
#                     score = int(score)  # Преобразуем строку в число
#                     total_score += score  # Добавляем к общей сумме
#                     count += 1  # Увеличиваем счетчик валидных оценок
#
#                     # Обновляем минимальную и максимальную оценки
#                     if score < min_score:
#                         min_score = score
#                     if score > max_score:
#                         max_score = score
#
#         # Если не было валидных оценок, ничего не делаем
#         if count == 0:
#             print("Нет валидных оценок в файле.")
#             return None, None, None
#
#         # Вычисляем средний балл
#         average_score = total_score / count
#
#         # Открываем файл в режиме добавления (не удаляем старые данные!)
#         with open(filename, "a") as file:
#             file.write(f"Minimum score is {min_score}\n")
#             file.write(f"Maximum score is {max_score}\n")
#             file.write(f"Average is {average_score}\n")
#
#         return min_score, max_score, average_score
#
#     except FileNotFoundError:
#         print("Ошибка: Файл не найден.")
#         return None, None, None
#
# # Главная функция программы
# def main():
#     filename = "scores.txt"
#     min_score, max_score, average_score = process_scores(filename)
#
#     if min_score is None:
#         return  # Если нет валидных данных, выходим
#
#     # Запрашиваем у пользователя имя студента
#     student_name = input("Whose score would you like to retrieve? --> ").strip()
#
#     # Открываем файл еще раз, чтобы найти нужную оценку
#     with open(filename, "r") as file:
#         found = False  # Флаг, нашли ли мы студента
#         while True:
#             name = file.readline().strip()  # Читаем имя
#             if not name:  # Если имя пустое, конец файла
#                 break
#
#             score = file.readline().strip()  # Читаем оценку
#             if is_valid_score(score) and name == student_name:  # Если имя совпадает и оценка валидная
#                 print(f"{student_name}'s score is {score}")
#                 found = True
#                 break  # Выходим из цикла
#
#     # Если не нашли студента
#     if not found:
#         print(f"{student_name} did not have a valid score")
#
#     # Выводим статистику
#     print(f"Minimum score is {min_score}")
#     print(f"Maximum score is {max_score}")
#     print(f"Average is {average_score}")
#
# # Запуск программы
# if __name__ == "__main__":
#     main()