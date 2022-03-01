#!/usr/bin/python3
"""console.py
Module  that contains the entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the console
    """
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        self.close()
        quit()

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        self.close()
        quit()

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
