import edit_database
import note_class

def delete(input_id):
    flag_deleted = False
    list_notes = edit_database.read_file()
    for note in list_notes:
        if input_id == note_class.Note.get_id(note):
            flag_deleted = True
            list_notes.remove(note)
            print("Заметка удалена")
    edit_database.write_list_to_file(list_notes, 'a')
    if flag_deleted == False:
        print("Такой заметки нет. Возможно вы ввели неверный id")