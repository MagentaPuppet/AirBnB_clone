#!/usr/bin/python3
"""Module for hbnb console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class that defines the console commands for the hbnb console"""

    # intro = 'Welcome to the HBNB console. Type help or ? to list commands.\n'
    prompt = '(hbnb)'

    # ----- basic console commands -----
    def do_quit(self, arg):
        """Quit command to exit the console\n"""

        print('Quitting the console')
        return True

    def do_EOF(self, arg):
        """Quit command to exit the console\n"""

        print('Quitting the console')
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel,
           saves it (to the JSON file) and prints the id
        """

        if arg == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            key = "{}.{}".format(arg, my_model.id)
            print(my_model.id)
            # if key not in storage.all():
            #     print("** an error occured **")
            # else:
            #     print("** instance created successfully **")
        else:
            if not arg:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
           based on the class name and id
        """

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name an id"""

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
                    # storage.reload()
                    # if key in storage.all():
                    #     print("** an error occured **")
                    # else:
                    #     print("** instance {} destroyed successfully **"
                    #           .format(key))

    def do_all(self, arg):
        """Prints all string representations of all instances
           based or not on the class name
        """

        if not arg or arg in storage.classes():
            all = []
            for i in storage.all().values():
                all += [i.__str__()]
            print(all)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
           by adding or updating the attribute
        """

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            length = len(args)
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif length < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    if length < 3:
                        print("** attribute name missing **")
                    else:
                        dict = storage.all()[key].to_dict()
                        if args[2] not in dict.keys():
                            print("** attribute not found **")
                        elif args[2] in ["id", "created_at", "updated_at"]:
                            print("** access to attribute <{}> denied **"
                                  .format(args[2]))
                        elif length < 4:
                            print("** value missing **")
                        else:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.save()
                            # storage.reload()
                            # if getattr(storage.all()[key], args[2]) != args[3]:
                            #     print("** an error occured **")
                            # else:
                            #     print("** attribute <{}> updated \
                            #           successfully **".format(args[2]))

    # ----- system overrides -----
    def emptyline(self):
        """Causes nothing to be executed when an empty line is run"""

        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
