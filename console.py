#!/usr/bin/python3
"""
file: console.py

This module contains the entry point of the command interpreter for 
the AirBnB clone project. The interpreter provids commands 
to manage objects like creating, updating and deleting instances.
"""

import cmd 
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """to handle the commands of the HBNB project and inherits 
    from cmd.Cmd to manage
    the command loop and user input
    """
    
    prompt = "(hbnb)"
    
    valid_classes = {
        "BaseModel":BaseModel,
        "User":User,
        "State" :State,
        "City" : City,
        "Amenity" :Amenity,
        "Place" :Place,
        "Review" :Review
    }

    #This method handles the quit command
    def do_quit(self, arg):
        """ Type quit to exit program """
        print()
        return True
    
    def do_EOF(self, arg): #This method handles End of File command (ctrl + D)
        """exit program when ctrl+D is pressed (end of file command)"""
        print()
        return True
    
    def emptyline(self):
        """ when an empty line is entered do nothing """
        pass

    def do_create(self, args):
        """ creates a new instance of BaseModel, saves it and prints the ID"""
        
        if not args:
            print("** class name missing **")
            return
        
        class_name = args.split()[0]
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.valid_classes[class_name]()
        new_instance.save()
        print(new_instance.id)


    def do_show(self, args):
        """ prints string representation an instance based on a class name and ID"""
        tokens = args.split()
        
        if len(tokens) == 0:
            print("** class name missing **")
            return

        if tokens[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        if len(tokens) == 1:
            print("** instance id missing **") #if the class name is provided but no Id
            return

            
            key = "{}.{}".format(tokens[0], tokens[1])
            obj = storage.all().get(key)
            
            if not obj:
                print("** no instance found **")
                
            else:
                print(obj)

    def do_destroy(self, args):
        """ deletes instance based on class name and id """

        tokens = args.split()
        
        if len(tokens) == 0:
            print("** class name missing **")
            return
        
        class_name = tokens[0]
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        
        if len(tokens) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(tokens[0], tokens[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()

        else:
                print("** no instance found **")


    def do_all(self, args):
        """ prints all instances of a class """

        if not args:
            objects = [str(obj) for obj in storage.all().values()]
            return
        # if class name is BaseModel print only BaseModel instances

        else:
            if args not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            objects = [str(obj) for key, obj in storage.all().items() if key.startswith(args)]
        print(objects)

    def do_update(self,args):
        """ updates an instance by adding or updating an attribute """

        tokens = args.split()
        
        if len(tokens) == 0:
            print("** class name missing **")
            return

        class_name = tokens[0]
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        if len(tokens) == 1:
            print("** instance id missing **")
            return
        

        key = "{}.{}".format(tokens[0], tokens[1])
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(tokens) == 2:
            print("** attribute name missing **")
            return

        if len(tokens) == 3:
            print("** value missing **")
            return

        attribute_name = tokens[2]
        attribute_value = tokens[3].strip('"')

        if attribute_value.isdigit():
            attribute_value = int(attribute_value)

        else:
            try:
                attribute_value = float(attribute_value)
            except ValueError:
                pass

            obj = obj_dict[key]
            setattr(obj, attribute_name, attribute_value)
            obj.save()
            key = tokens[0] + "." + tokens[1]


# This block makes sure the program only runs when the script is executed directly
if __name__ == "__main__":
    HBNBCommand().cmdloop()  #starts the command loop
