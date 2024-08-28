#!/usr/bin/python3
"""
This file defines the console class
which will serve as basis of the entire project
"""
import cmd
import sys
import json
from models.engine.file_storage import FileStorage
from utilities_for_console import *
from models import storage

# Global variable of existing classes.
classes = storage.models


class UniConnectCommand(cmd.Cmd):
    """
    The console - A simple command interpreter that manages objects
    for the UniConnect project.
    All in interaction with the system are done via this class.
    """

    prompt = "(UniConnect) "

    def do_quit(self, line_arg):
        """ Quits command to exit the program\n """
        return True

    def do_EOF(self, line_arg):
        """Exit command that quits the program\n """
        return True

    def emptyline(self):
        """ Do nothing when an empty line is entered\n """
        pass
    # -------------------------------------------------------------------------

    def do_create(self, line_arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id .
        Usage:
            $ create BaseModel
        """
        if line_arg:
            args = line_arg.split()
            if len(args) >= 1:
                class_name = args[0]
                new_model = create_object(class_name)
                if new_model:
                    attribute = parse_param(line_arg)
                    for name, value in attribute.items():
                        setattr(new_model, name, value)
                    new_model.save()
                    print("{}".format(new_model.id))
                else:
                    print("** class doesn't exist **")
                    return
            else:
                print("** Too many argument for create **")
                return
        else:
            print("** class name missing **")

    # -------------------------------------------------------------------------

    def do_show(self, line_arg):
        """
        Prints the string representation of an instance based on
        class name and id.
        Usage:
             $ show BaseModel 1234-1234-1234
        """
        if not line_arg:
            print("** class name missing **")
            return

        all_objects = storage.all()
        args = line_arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            class_name = args[0]
            print("** instance id missing **")
            return
        elif len(args) == 2:
            class_name = args[0]
            obj_id = args[1]
            class_key = f"{class_name}.{obj_id}"

            if class_key in all_objects:
                print(all_objects[class_key])
            else:
                print("** no instance found **")
                return
        else:
            print("** Too many argument for show")
            return

    # -------------------------------------------------------------------------

    def do_destroy(self, line_arg):
        """
        Deletes an instance based on the class name and id
        Usage:
            $ destroy BaseModel 1234-1234-1234
        """

        if not line_arg:
            print("** class name missing **")
            return
        all_objects = storage.all()
        args = line_arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if check_object(args, all_objects) is False:
            print("** no instance found **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            class_name = args[0]
            obj_id = args[1]
            class_key = f"{class_name}.{obj_id}"
            if class_name in classes:
                if class_key in all_objects.keys():
                    del all_objects[class_key]
                    FileStorage.__objects = all_objects
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            else:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for destroy **")
            return

    # -------------------------------------------------------------------------

    def do_all(self, line_arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        Usage:
            $ all BaseModel
            or
            $ all
        """
        all_objects = storage.all()
        if line_arg:
            args = line_arg.split()
            if len(args) == 1:
                class_name = args[0]
                if class_name not in classes:
                    print("** class doesn't exist **")
                    return
                for obj_key, obj in all_objects.items():
                    if obj_key.startswith(class_name):
                        print(obj)
            else:
                print("** Too many argument for all **")
                return

        else:
            for key in all_objects:
                print(all_objects[key])

    # -------------------------------------------------------------------------

    def do_update(self, line_arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Usage:
            $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if not line_arg:
            print("** class name missing **")
            return
        all_objects = storage.all()
        args = line_arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if check_object(args, all_objects) is False:
            print(args)
            print("** no instance found **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        elif len(args) == 4:
            update_obj_attr(args, all_objects, storage)
        else:
            print("** Too many argument for update **")
            print(args)

    # -------------------------------------------------------------------------

    def default(self, arg):
        """ overides the default method to handle unrecognised commands """
        if arg:
            args = arg.split('.')
            if ('.' in arg and '(' in arg and args[0] in classes
                    and args[1][-1:] == ")"):
                # if args[0] in classes and re.match(pattern, arg[1]):
                return self.handle_unregistered_command(arg)

        return cmd.Cmd.default(self, arg)

    def handle_unregistered_command(self, arg):
        """ handles other methods """
        if arg:
            args = arg.split('.')
            obj_class = args[0]
            method = args[1]
            if method == "all()":
                self.all_instances(arg)
            elif method == "count()":
                self.count_instances(arg)
            elif ((method.startswith("show(") or method.startswith("destroy(")
                   or method.startswith("update(")) and method[-1:] == ')'):
                self.show_destroy_update_instances(arg)
            else:
                print("** Invalid syntax **")

    def all_instances(self, arg):
        """
         retrieve all instances of a class by using: <class name>.all()
        """
        if arg:
            token = arg.split('.')
            obj_class = token[0]
            method = token[1]
            if obj_class in classes:
                if method == "all()":
                    self.do_all(f"{obj_class}")

                else:
                    print("** Invalid syntax **")
                    return

    def count_instances(self, arg):
        """ retrieve the number of instances of a class:
            <class name>.count()
        """
        if arg and len(arg.split()) == 1:
            count = 0
            args = arg.split('.')
            obj_class = args[0]
            method = args[1]
            if obj_class in classes:
                if method == "count()":
                    all_object = storage.all()
                    for key, obj in all_object.items():
                        if key.startswith(obj_class):
                            count += 1
                    print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for count **")

    def show_destroy_update_instances(self, arg):
        """ retrieve an instance based on its ID: <class name>.show(<id>) """
        if arg:
            args = arg.split('.')
            obj_class = args[0]
            method = args[1]
            if obj_class in classes:
                obj_attr = extract_attr(method)
                # print(obj_attr)
                # if obj_attr.startswith('"'):
                # obj_attr = obj_attr.replace('"', '')
                if method.startswith("show(") and method[-1:] == ")":
                    self.do_show(f"{obj_class} {obj_attr}")
                elif method.startswith("destroy(") and method[-1:] == ")":
                    self.do_destroy(f"{obj_class} {obj_attr}")
                elif method.startswith("update(") and method[-1:] == ")":
                    attr = custom_split(obj_attr)
                    id = attr[0]
                    if id.startswith('"'):
                        id = attr[0].replace('"', '')
                    attribute = attr[1]
                    attr_dict = {}
                    if attribute.startswith("{"):
                        attribute = attr[1].replace("'", '"')
                        dict_str = f"{attribute}"
                        attr_dict = json.loads(dict_str)
                    elif attribute.startswith('"'):
                        attr_name = attribute.replace('"', '')
                        value = attr[2]
                        if value.startswith('"'):
                            value = attr[2].replace('"', '')
                        attr_dict[attr_name] = value
                    for attribute, value in attr_dict.items():
                        self.do_update(f"{obj_class} {id} {attribute} {value}")
                else:
                    print("** Invalid syntax **")
            else:
                print("** class doesn't exist **")
        else:
            print("** me - Too many argument **")


def run_interactive_mode():
    """ Runs the console in interactive mode """
    UniConnectCommand().cmdloop()


def run_non_interactive_mode():
    """ Runs the console in non interactive mode """
    commands = sys.argv[1:]
    for command in commands:
        try:
            UniConnectCommand().onecmd(command)

        except Exception as e:
            print("Error executing {} : {}".format(command, e))


if __name__ == '__main__':
    UniConnectCommand().cmdloop()

# -----------------------------------------------------------------------------
