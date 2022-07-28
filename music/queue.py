
class Queue:
    data = None

    def __init__(self):
        self.data = []

    def add(self, source):
        self.data.append(source)

    def pop(self):
        if len(self.data) == 0:
            return None

        source = self.data[0]
        self.data = self.data[1:]

        return source

    def get_head(self):
        if len(self.data) == 0:
            return None

        return self.data[0]

