import edit_database
import note_class


def checkInList(input_id):
    list_notes = edit_database.read_file()
    for note in list_notes:
        if input_id == note_class.Note.get_id(note):
            return True