assistant="What can i do for you?"

name_input="\tInsert the name of a note\n"

text_input="\n\tInsert the text\n Empty row will finish writing"

greeting="\t\tHello, Blyad\n"

menu=["Here is a list of your possibilities:\n",
      "all - print all of your notes",
      "create - create new note",
      "find - seek for a note",
      "change - rewrite a note",
      "delete - delete a note",
      "bin - print all existed notes in bin",
      "quit - to finish it",
      "help - to get help notes"]

bin_menu=["There in Bin you can do next things:", 
          "all - show all existed in bin notes",
          "delete - delete a note",
          "restore - restore a note from the bin",
          "clear - clear the bin",
          "help - to get help notes",
          "quit - to get back to Note Page"]
input_menu=">>\t"

exit="print 'stop' to stop"


def seek(self,option: str="find"):
      return "what are you want to {option}? "

def approvement(self, name: str, option: str="delete"):
      return "are you shure you want to {option} {name}?\nprint 'yes' or 'y' "