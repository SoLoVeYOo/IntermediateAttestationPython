import edit_database
import note_class


def edit(input_id, new_title, new_text):
    list_notes = edit_database.read_file()
    for note in list_notes:
        if input_id == note_class.Note.get_id(note):
            note_class.Note.set_title(note, new_title)
            note_class.Note.set_text(note, new_text)
            note_class.Note.set_date(note)
            print("Заметка изменена")
    edit_database.write_list_to_file(list_notes, 'a')