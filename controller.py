import interface
from notesManager import NotesManager
from binManager import BinManager
import time
from note import Note


def start(state: bool):
    NM=NotesManager()
    BM=BinManager()
    is_bin=False

    interface.greeting()
    NM.store_file()
    menu=interface.menu()
    match menu:
        case "all":
            for i, item in enumerate(NM.store):
                if item:
                    print(f"{i+1})\twhat\t{item.name}")

        case "find":
            name=interface.seek(menu)
            res=NM.find(name)
            interface.show_names(res)


        case "create":
            note=interface.create()
            if note:
                NM.store.append(note)
                NM.add(note)
            

        case "change":
            name=interface.seek(menu)
            res=NM.find(name)
            interface.show_names(res)
            choise=interface.choose()
            text=interface.text_input()
            res[choise].text=text
            

        case "delete":
            name=interface.seek(menu)
            answer=interface.approvement()
            if answer:
                BM.add(NM.delete)
                NM.update()
            

        case "bin":
            pass

        case "help":
            pass

        case "quit":
            pass
        
    NM.all()
    # for n in NM.store:
    #     print(n)
    # note=NM.newNote()
    # NM.add(note)
    # print(note)

    return