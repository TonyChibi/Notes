import interface
from notesManager import NotesManager
from binManager import BinManager
import time
from note import Note
class Controller():
    def __init__(self):
        NM=NotesManager()
        BM=BinManager()
        is_bin=False


    def start(self,state: bool):
       

        interface.greeting()
        self.NM.store_file()
        menu=interface.menu()
        match menu:
            case "all":
                for i, item in enumerate(self.NM.store):
                    if item:
                        print(f"{i+1})\t{item.name}")

            case "find":
                self.find(menu)


            case "create":
                note=interface.create()
                if note:
                    self.NM.store.append(note)
                    self.NM.add(note)
                

            case "change":
                name=interface.seek(menu)
                res=self.NM.find(name)
                interface.show_names(res)
                choise=interface.choose_number(res.length)
                text=interface.text_input()
                res[choise].text=text
                

            case "delete":
                name=interface.seek(menu)
                answer=interface.approvement()
                if answer:
                    self.BM.add(self.NM.delete(answer))
                    self.NM.update()
                

            case "bin":
                pass

            case "help":
                pass

            case "quit":
                pass
            

    def find(self, menu):
        name=interface.seek(menu)
        res=self.NM.find(name)
        interface.show_names(res)
        num=int(interface.choose_number(res.length))-1
        interface.show_text(res[num])   