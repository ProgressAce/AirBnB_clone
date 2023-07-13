#!/usr/bin/python3
import cmd
# from models import storage
# uncomment storage import once its available
from models.base_model import BaseModel
"""This is the Console

The command line interpreter for our AirBnB clone
"""


class HBNBCommand(cmd.Cmd):
    """The console"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit the program (Control d)\n"""
        print()
        return True

    def emptyline(self):
        """An empty line + Enter does not execute any command"""
        pass

    def help_help(self):
        print(''.join([
           'List available commands with "help"',
           ' or detailed help with "help hbnb".\n'
        ]))

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg == BaseModel:
            pass  # do later
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print(''.join([
            'Creates a new instance of BaseModel, ',
            'saves it (to the JSON file) and prints the id.\n',
            '\nExample:\n',
            '\n$ create BaseModeli\n'
        ]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
