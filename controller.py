import interface
from notesManager import NotesManager
from binManager import BinManager
import time
from note import Note
class Controller():

    
    def start(self,state: bool):
        NM=NotesManager()
        BM=BinManager()
        is_bin=False
        obj=NM

        interface.greeting()
        NM.store_file()

        interface.menu()
        while state:
            now=time.time()
            print(time.ctime(now))

            message=interface.assistant()
            match message:
                case "all":
                    interface.show_names(*obj.store)
                  

                case "find":
                    self.find(obj, message)


                case "create":
                    note=interface.create()
                    if note:
                        NM.store.append(note)
                        NM.add(note)
                    

                case "change":
                    if is_bin:
                        res=self.find(obj, message)
                        text=interface.text_input()
                        name=interface.name_input()
                        answer=interface.approvement(res.name,message)
                        if answer: 
                            self.restore(BM.change(res, name,text, time.time()), BM, NM)

                    else:
                        res=self.find(obj, message)
                        if res:
                            text=interface.text_input()
                            name=interface.name_input()
                            answer=interface.approvement(res.name,message)
                            if answer:
                                NM.change(res,name,text,time.time())
                                NM.update()
                            
                    

                case "delete":
                    note=self.find(obj, message)
                    if note:
                        answer=interface.approvement(note.name, message)
                        if answer:
                            BM.add(NM.delete(note))
                            NM.update()
                    

                case "bin":
                    obj=BM
                    BM.store_file()
                    BM.update()
                    is_bin=True
                    interface.show_names(*obj.store)
                    pass

                case "help":
                    if is_bin:
                        interface.bin_menu()
                    else:
                        interface.menu()

                case "clear":
                    if is_bin:
                        BM.clear()
                        BM.store()

                case "restore":
                    if is_bin:
                        note=self.find(BM, message)
                        if note:
                            self.restore(note,BM, NM)
                    

                case "quit":
                    if is_bin:
                        obj=NM
                        is_bin=False
                    else:
                        state=False
                    
            


    def find(self,obj: NotesManager , option: str = "find"):
        name=interface.seek(option)
        res=obj.find(name)
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
           

    def restore(self, note: Note ,bm: BinManager, nm: NotesManager):
        nm.add(note)
        nm.store_file()
        bm.delete(note)
        bm.update()
