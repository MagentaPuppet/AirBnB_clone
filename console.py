#!/usr/bin/python3
"""Module for hbnb console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines the console commands for the hbnb console"""

    intro = 'Welcome to the HBNB console. Type help or ? to list commands.\n'
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the console\n"""

        print('Quitting hbnb console')
        return True

    def do_EOF(self, arg):
        """Quit command to exit the console\n"""

        print('Quitting the console')
        return True

    def emptyline(self):
        """Causes nothing to be executed when an empty line is run"""

        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
