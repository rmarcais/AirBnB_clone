#!/usr/bin/python3
"""console.py
Module  that contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel
import models.engine.file_storage


class HBNBCommand(cmd.Cmd):
    """This class defines the console
    """
    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """Method to only print the message once"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        quit()

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id
        """
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            var = BaseModel()
            var.save()
            print(hello.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id
        """
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            var = BaseModel()
            var.save()
            print(hello.id)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name
        """

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
