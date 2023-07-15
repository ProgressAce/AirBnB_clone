#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
"""This is the Console

The command line interpreter for our AirBnB clone
"""
all_objs = models.storage.all()


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
        elif arg == "BaseModel":
            new_base = BaseModel()
            new_base.save()
            print(new_base.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print(''.join([
            'Creates a new instance of BaseModel, ',
            'saves it (to the JSON file) and prints the id.\n',
            '\nExample:\n',
            '\n$ create BaseModeli\n'
        ]))

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        arg_list = arg.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("class doesn't exist")
        elif len(arg_list) == 1:
            print("** instance id missing *")
        elif arg_list[1] != "1234":  # iplement later
            print("** no instance found **")
        else:
            pass  # implement show action later

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234
        """
        arg_list = arg.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("class doesn't exist")
        elif len(arg_list) == 1:
            print("** instance id missing *")
        elif arg_list[1] != "1234":  # iplement later
            print("** no instance found **")
        else:
            pass  # implement show action later

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        The printed result is a list of strings

        Ex: $ all BaseModel or $ all.
        """
        arg_list = arg.split()
        if not arg_list:
            print("string representation of all instances (list)")
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist *")
        else:
            print("str repre. of all inst. of a part. class (list)")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        arg_list = arg.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] != "BaseModel":
            print("class doesn't exist")
        elif len(arg_list) == 1:
            print("** instance id missing *")
        elif arg_list[1] != "1234":  # iplement later
            print("** no instance found **")
        elif len(arg_list) == 2:
            print("** attribute name missing *")
        elif len(arg_list) == 3:
            print("** value missing *")
        else:
            pass  # implement valid update action later


if __name__ == '__main__':
    HBNBCommand().cmdloop()
