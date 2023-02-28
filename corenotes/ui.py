import keyboard
import note_class


def create_note():
    note = new_note()
    return note_class.Note(title=note[0], text=note[1])


def new_note():
    title = ''
    text = ''
    while len(title) < 3:
        print("<Заголовок должен содержать от 3 символов>")
        title = input("Введите 'Заголовок' заметки: ")
    while len(text) < 3:
        print("<Заметка должна содержать от 3 символов>")
        text = input("Введите 'Текст' заметки: ")
    return (title,text)


def menu():
    print()
    print("Выберите задачу:")
    print("1 - для вывода всех заметок\n"
        "2 - для добавления заметки\n"
        "3 - для удаления заметки\n"
        "4 - для редактирования заметки\n"
        "5 - для выборки по дате\n"
        "6 - показать элемент по id\n"
        "7 - для выхода\n")


def continue_work():
    print("\nНажмите пробел для продолжения...")
    keyboard.wait('space')