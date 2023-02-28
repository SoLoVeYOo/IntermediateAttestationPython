import edit_database
import note_class


def add(new_note):
    list_notes = edit_database.read_file()
    for note in list_notes:
        if note_class.Note.get_id(new_note) == note_class.Note.get_id(note):
            note_class.Note.set_id(new_note)
    list_notes.append(new_note)
    edit_database.write_list_to_file(list_notes, 'a')
    print("Заметка добавлена")