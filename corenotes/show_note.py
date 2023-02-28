import edit_database
import note_class


def show():
    try:
        list_notes = edit_database.read_file()
        for notes in list_notes:
            print()
            print(note_class.Note.to_show(notes))
    except Exception:
        print("\nНет ни одной задачи\n")


def show_by_date(input):
    flag_empty = True
    list_notes = edit_database.read_file()
    for note in list_notes:
        if input in note_class.Note.get_date(note):
            print()
            print(note_class.Note.to_show(note))
            flag_empty = False
    if flag_empty == True:
        print("Задач не найдено")


def show_by_id(input):
    flag_empty = True
    list_notes = edit_database.read_file()
    for note in list_notes:
        if input == note_class.Note.get_id(note):
            print()
            print(note_class.Note.to_show(note))
            flag_empty = False
    if flag_empty == True:
        print("Задач не найдено")

def show_all_by_id():
    try:
        list_notes = edit_database.read_file()
        for note in list_notes:
            print("id: " + note_class.Note.get_id(note))
    except Exception:
        print("\nНет ни одной задачи\n")