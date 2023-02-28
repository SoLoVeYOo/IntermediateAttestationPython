import ui
import add_note
import edit_note
import delete_note
import show_note
import check_note


def start():
    user_input = '0'
    print('Добро пожаловать в программу "Notes"')

    while user_input != '7':
        ui.menu()
        user_input = input("Введите номер задачи: ").strip()

        if user_input == '1':
            show_note.show()
            ui.continue_work()

        if user_input == '2':
            note = ui.create_note()
            add_note.add(note)
            ui.continue_work()

        if user_input == '3':
            show_note.show()
            print()
            delete_note.delete(input("Введите id заметки: "))
            ui.continue_work()

        if user_input == '4':
            show_note.show()
            print()
            user_input = input("Введите id заметки: ")
            if check_note.checkInList(user_input):
                change_note = ui.new_note()
                edit_note.edit(user_input, change_note[0], change_note[1])
            else:
                print("Такой заметки нет. Возможно вы ввели неверный id")
            ui.continue_work()

        if user_input == '5':
            show_note.show_by_date(input("Введите дату в формате dd.mm.yyyy: "))
            ui.continue_work()

        if user_input == '6':
            show_note.show_all_by_id()
            print()
            show_note.show_by_id(input("Введите id заметки: "))
            ui.continue_work()

        if user_input == '7':
            print("Exit")
            break