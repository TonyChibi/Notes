from notesManager import NotesManager
class BinManager(NotesManager):
    def __init__(self, path: str="notesBin.txt", name: str="bin"):
            super().__init__(path, name)

    def is_inspired(self, created:float, current: float):
        insp_date=86400*30 # 30 days in seconds
        if current-created>=insp_date:
            return True
        else:
             return False
    

    def refresh(self):
        return
    
    def change (self):
        return
    
    def clear(self):
        with open(self.path, "w", encoding="utf-8") as file:
             file.write("")

