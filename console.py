#!/usr/bin/python3
"""console.py
Module  that contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models.engine.file_storage
import models
import re


class HBNBCommand(cmd.Cmd):
    """This class defines the console
    """
    prompt = '(hbnb) '
    file = None
    c = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]

    def emptyline(self):
        """Method to only print the message once"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class name> or <class name>.create()
        """
        args = line.split(' ')
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.c:
            print("** class doesn't exist **")
        else:
            var = eval(args[0])()
            var.save()
            print(var.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id
        Usage: show <class name> <id> or <class name>.show(<id>)
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.c:
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
        Usage: destroy <class name> <id> or <class name>.destroy(<id>)
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.c:
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
        """Prints all string representation of all instances based
        or not on the class name
        Usage: all or all <class name> or <class name>.all()
        """
        args = line.split()
        if len(args) >= 1 and args[0] not in HBNBCommand.c:
            print("** class doesn't exist **")
        else:
            dico = models.storage.all()
            my_list = []
            for k, v in dico.items():
                if len(args) == 0:
                    my_list.append(str(dico[k]))
                elif type(v) is eval(args[0]):
                    my_list.append(str(dico[k]))
            print(my_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>" or
        <class name>.update(<id>, <attribute name>, "<attribute value>")
        """
        args = line.split()
        ivan = line.partition('"')
        arguments = line.split('"')[1::2]
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.c:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                dico = models.storage.all()
                foo = dico[args[0] + '.' + args[1]]
            except Exception:
                print("** no instance found **")
                return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        if len(arguments) >= 2:
            args[2] = arguments[0]
            args[3] = arguments[1]
        elif len(arguments) == 1:
            if args[2][0] == '"':
                args[2] = arguments[0]
            else:
                args[3] = arguments[0]

        setattr(foo, args[2].strip('"'), args[3].strip('"'))
        foo.save()

    def do_count(self, line):
        """Count the number of instances
        Usage: count <class name> or <class name>.count()
        """
        args = line.split()
        if len(args) >= 1 and args[0] not in HBNBCommand.c:
            print("** class doesn't exist **")
        elif len(args) >= 1:
            dico = models.storage.all()
            my_list = []
            for k, v in dico.items():
                if type(v) is eval(args[0]):
                    my_list.append(str(dico[k]))
            print(len(my_list))
        else:
            print("** class name missing **")

    def default(self, line):
        """Method called when the command isn't reconnized"""
        methods = {
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update,
            "count": self.do_count
        }
        match_point = re.search(r"\.", line)
        if match_point is not None:
            """Take the parts before and after the point"""
            two_parts = [line[:match_point.span()[0]],
                         line[match_point.span()[1]:]]

            match_par = re.search(r"\((.*?)\)", two_parts[1])
            """Search () in the part after the point"""
            if match_par is not None:
                command = [two_parts[1][:match_par.span()[0]],
                           match_par.group()[1:-1]]
                """Keep the command and the id"""

                if command[0] in methods.keys():
                    if command[0] == "update":
                        replacing = command[1].replace(",", " ")
                        """Remove the , between the ()"""
                        newline = "{} {}".format(two_parts[0], replacing)
                        return methods[command[0]](newline)
                    elif command[0] != "update":
                        newline = "{} {}".format(two_parts[0],
                                                 command[1])
                        return methods[command[0]](newline)
        print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
