#!/usr/bin/python3
"""console.py
Module  that contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel
import models.engine.file_storage
import models


class HBNBCommand(cmd.Cmd):
    """This class defines the console
    """
    prompt = '(hbnb) '
    file = None

    def emptyline(self):
        """Method to only print the message once"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        quit()

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id
        """
        args = line.split(' ')
        if len(args)  == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            var = eval(args[0])()
            var.save()
            print(var.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id
        """
        args = line.split()
        if len(args)  == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                dico = models.storage.all()
                print(dico[args[0] + '.' + args[1]])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        if len(args)  == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                dico = models.storage.all()
                del(dico[args[0] + '.' + args[1]])
                models.storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        """
        args = line.split()
        if len(args) >= 1 and args[0] != "BaseModel":
                print("** class doesn't exist **")
        else:
            dico = models.storage.all()
            my_list = []
            for k, v in dico.items():
                my_list.append(str(dico[k]))
            print(my_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
