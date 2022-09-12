#!/usr/bin/python3

import cmd, sys


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the HBNB console. Type help or ? to list commands.\n'
    prompt = '(hbnb)'
    file = None

    def do_quit(self, arg):
        'Quit command to exit the console\n'
        print('Quitting hbnb console')
        return True

    def do_EOF(self, arg):
        'Quit command to exit the console\n'
        print('Quitting the console')
        return True

    def emptyline(self):
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
