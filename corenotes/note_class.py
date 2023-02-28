from datetime import datetime
import uuid


class Note:
    def __init__(self, id=str(uuid.uuid1())[0:3], title="текст", text="текст",
                date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.text = text
        self.date = date

    def get_id(note):
        return note.id

    def get_date(note):
        return note.date

    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    def set_title(note, title):
        note.title = title

    def set_text(note, text):
        note.text = text

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.text + ';' + note.date

    def to_show(note):
        return 'id: ' + note.id + '\n'\
            + 'Заголовок: ' + note.title + '\n'\
            + 'Текст: ' + note.text + '\n'\
            + 'Дата создания: ' + note.date