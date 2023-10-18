class snap:
    def chat(self):
        print("This is chatting mode")
    
    def videocall(self):
        print("This is videocalling mode")


class watsapp(snap):
    def status(self):
        print("You are seeing status")


obj = watsapp()
obj.chat()