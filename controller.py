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
            NM.find(name)

            pass

        case "create":
            note=interface.create()
            if note:
                NM.store.append(note)
                NM.add(note)
            pass

        case "change":
            pass

        case "delete":
            pass

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