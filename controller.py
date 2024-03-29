import interface
from notesManager import NotesManager
from binManager import BinManager
import time
from note import Note
class Controller():

    NM=NotesManager()
    BM=BinManager()
    is_bin=False
    obj=NM
    def start(self,state: bool):
       

        interface.greeting()
        self.NM.store_file()
        
        interface.menu()
        while state:
            message=interface.assistant()
            match message:
                case "all":
                    interface.show_names(*self.obj.store)
                    # for i, item in enumerate(self.obj.store):
                    #     if item:
                    #         print(f"{i+1})\t{item.name}")

                case "find":
                    self.find(message)


                case "create":
                    note=interface.create()
                    if note:
                        self.NM.store.append(note)
                        self.NM.add(note)
                    

                case "change":
                    name=interface.seek(message)
                    res=self.NM.find(name)
                    interface.show_names(res)
                    choise=interface.choose_number(res.length)
                    text=interface.text_input()
                    res[choise].text=text
                    

                case "delete":
                    name=interface.seek(message)
                    answer=interface.approvement()
                    if answer:
                        self.BM.add(self.NM.delete(answer))
                        self.NM.update()
                    

                case "bin":
                    pass

                case "help":
                    interface.menu()
                    

                case "quit":
                    state=False
                    
            

    def find(self, message: str):
        name=interface.seek(message)
        res=self.NM.find(name)
        if res:
            interface.show_names(*res)
            num=int(interface.choose_number(len(res)))-1
            if num:
                interface.show_text(res[num])
                return res[num]
        else:
            interface.not_found()
           