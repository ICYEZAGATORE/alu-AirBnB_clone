#!/usr/bin/python3
import cmd 

class HBNBCommand(cmd.Cmd):
    """to handle the commands of the HBNB project """
    prompt = "(hbnb)"
    
    #This method handles the quit command
    def do_quit(self, arg):
        """ Type quit to exit program """
        print()
        return True
    
    #This method handles End of File command (ctrl + D)
    def do_EOF(self, arg):
        """exit program when ctrl+D is pressed (end of file command)"""
        print()
        return True
    
    #This method is called when the user presses ENTER without typing anything
    def emptyline(self):
        """ when an empty line is entered do nothing """
        pass


# This block makes sure the program only runs when the script is executed directly
if __name__ == "__main__":
    HBNBCommand().cmdloop()  #starts the command loop
