import note_class


# def writeTofile(note, mode):
#     file = open ("notesDatabase.csv", mode = mode, encoding='utf-8')
#     stringNote = note_class.Note.to_string(note)
#     file.write(stringNote)
#     file.write('\n')
#     file.close


def write_list_to_file(list_note, mode):
    file = open ("notesDatabase.csv", mode = 'w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open ("notesDatabase.csv", mode = mode, encoding='utf-8')
    for note in list_note:
        str_note = note_class.Note.to_string(note)
        file.write(str_note)
        file.write('\n')
    file.close


def read_file():
    try:
        file = open("notesDatabase.csv", 'r', encoding='utf-8')
        notes = file.read().strip().split("\n")
        list_notes =[]
        for row in notes:
            splited_note = row.split(';')
            note = note_class.Note(id = splited_note[0], title=splited_note[1], text = splited_note[2], date = splited_note[3])
            list_notes.append(note)
    except Exception:
        print("Нет заметок")
    finally:
        return list_notes