#!/usr/bin/python3
import cmd
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
