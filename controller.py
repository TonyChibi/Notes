import interface
from notesManager import NotesManager
from binManager import BinManager
import time
from note import Note


def start(state: bool):
    NM=NotesManager()
    BM=BinManager()
    is_bin=False
    NM.store_file()
    NM.all()
    for n in NM.store:
        print(n)
    # note=NM.newNote()
    # NM.add(note)
    # print(note)

    return