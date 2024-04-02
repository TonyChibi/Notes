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
            now=time.time()
            print(time.ctime(now))

            message=interface.assistant()
            match message:
                case "all":
                    interface.show_names(*self.obj.store)
                  

                case "find":
                    self.find(message)


                case "create":
                    note=interface.create()
                    if note:
                        self.NM.store.append(note)
                        self.NM.add(note)
                    

                case "change":
                    res=self.find(message)
                    if res:
                        text=interface.text_input()
                        name=interface.name_input()
                        answer=interface.approvement(res.name,message)
                        if answer:
                            self.NM.change(res,name,text,time.time())
                            self.NM.update()
                            
                    

                case "delete":
                    name=interface.seek(message)
                    answer=interface.approvement()
                    if answer:
                        self.BM.add(self.NM.delete(answer))
                        self.NM.update()
                    

                case "bin":
                    self.obj=self.BM
                    pass

                case "help":
                    interface.menu()
                    

                case "quit":
                    state=False
                    
            


    def find(self, option: str = "find"):
        name=interface.seek(option)
        res=self.NM.find(name)
        if len(res)>1:
            interface.show_names(*res)
            num=int(interface.choose_number(len(res)))-1
            if num>=0:
                interface.show_text(res[num])
                return res[num]
            else:
                return False
        elif len(res)==1:
            interface.show_text(*res)
            return res[0]
        else:
            interface.not_found()
           