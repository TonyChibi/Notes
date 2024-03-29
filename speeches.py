assistant="What can i do for you?"

bin_menu=["There in Bin you can do next things:", 
          "all - show all existed in bin notes",
          "delete - delete a note",
          "restore - restore a note from the bin",
          "clear - clear the bin",
          "help - to get help notes",
          "quit - to get back to Note Page"]

choise="choose the index of a note"

exit="print 'stop' to stop"

greeting="\t\tHello, Blyad\n"

name_input="Insert the name of a note"

not_found="I cannot find anything"

text_input="\n\tInsert the text\n Empty row will finish writing"



menu=["Here is a list of your possibilities:\n",
      "all - print all of your notes",
      "create - create new note",
      "find - seek for a note",
      "change - rewrite a note",
      "delete - delete a note",
      "bin - print all existed notes in bin",
      "quit - to finish it",
      "help - to get help notes"]


input_menu=">>\t"




def seek(self,option: str="find"):
      return f"what are you want to {option}? "

def approvement(self, name: str, option: str="delete"):
      return "are you shure you want to {option} {name}?\nprint 'yes' or 'y' "

