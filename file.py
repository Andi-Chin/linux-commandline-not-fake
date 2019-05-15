from sett import Sett


class File():
    def __init__(self, name, text):
        self.name = name
        self.text = text
    def cat(self):
        print(self.text)
