class parent:
    def parent(self):
        print("Hello parent class ")


class child(parent):
    def parent(self):
        super().parent()
        print("Hello child class ")

obj =child()
obj.parent()