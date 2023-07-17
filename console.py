#!/usr/bin/python3
"""This is the Console

The command line interpreter for our AirBnB clone
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
all_objs = models.storage.all()
"""Dictionary of all objects"""
classes = {'BaseModel': BaseModel, 'User': User}
"""Dictionary of all model classes"""


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
        Ex: $ create BaseModel or $ create User
        """
        if not arg:
            print("** class name missing **")
        elif arg in classes:
            new_obj = classes[arg]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print('\n'.join([
            'Creates a new instance of BaseModel,',
            'saves it (to the JSON file) and prints the id.',
            'Example:',
            '$ create BaseModel',
            'or',
            '$ create User'
        ]))

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        Ex: $ show User 1234-1234-1234
        """
        arg_list = arg.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif f'{arg_list[0]}.{arg_list[1]}' not in all_objs:
            print("** no instance found **")
        else:
            key = f'{arg_list[0]}.{arg_list[1]}'
            print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234
        """
        arg_list = arg.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif f'{arg_list[0]}.{arg_list[1]}' not in all_objs:
            print("** no instance found **")
        else:
            key = f'{arg_list[0]}.{arg_list[1]}'
            del all_objs[key]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        The printed result is a list of strings

        Ex: $ all BaseModel or $ User or $ all.
        """
        arg_list = arg.split()
        if not arg_list:
            all_list = [str(all_objs[key]) for key in all_objs]
            print(all_list)
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        else:
            all_list = [str(all_objs[key]) for key in all_objs if arg_list[0]
                        in key]
            print(all_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Ex: $ update User 1234-1234-1234 email "aibnb@mail.com"
        """
        arg_list = arg.split()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif f'{arg_list[0]}.{arg_list[1]}' not in all_objs:
            print("** no instance found **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            key = f'{arg_list[0]}.{arg_list[1]}'
            value = arg_list[3].strip('"')
            att_name = arg_list[2]
            if att_name in all_objs[key].__dict__:
                try:
                    value = type(all_objs[key].__dict__[att_name])(value)
                    all_objs[key].__dict__[att_name] = value
                    all_objs[key].save()
                except ValueError:
                    pass
            else:
                all_objs[key].__dict__[att_name] = value
                all_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
