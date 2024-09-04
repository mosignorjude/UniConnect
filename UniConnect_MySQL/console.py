#!/usr/bin/python3
"""
This file defines the console class
which will serve as basis of the entire project
"""
import cmd
import sys
import json
from models import storage, User, Student, Lecturer, Course, Enrollment, Grade, LectureNotes, Appointment, Payment, CourseLecturers
from utilities_for_console import *

# Global variable of existing classes.
classes = {
    'User': User,
    'Student': Student,
    'Lecturer': Lecturer,
    'Course': Course,
    'Enrollment': Enrollment,
    'Grade': Grade,
    'LectureNotes': LectureNotes,
    'Appointment': Appointment,
    'Payment': Payment,
    'CourseLecturers': CourseLecturers
}

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
        Creates a new instance of BaseModel, saves it (to the database)
        and prints the id.
        Usage:
            $ create BaseModel
        """
        if line_arg:
            args = line_arg.split()
            if len(args) >= 1:
                class_name = args[0]
                if class_name in classes:
                    new_model = classes[class_name]()
                    attribute = parse_param(line_arg)
                    required_attributes = ['first_name', 'last_name', 'email', 'password', 'user_type']
                    
                    # Add required attributes for Lecturer
                    if class_name == 'Lecturer':
                        required_attributes.extend(['department', 'program', 'contact', 'rank'])

                    missing_attributes = [attr for attr in required_attributes if attr not in attribute]

                    if missing_attributes:
                        print(f"** Missing required attributes: {', '.join(missing_attributes)} **")
                        return

                    for name, value in attribute.items():
                        setattr(new_model, name, value)
                    storage.session.add(new_model)
                    storage.session.commit()
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

        args = line_arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            class_name = args[0]
            obj_id = args[1]
            obj = storage.session.get(classes[class_name], obj_id)
            if obj:
                print(obj)
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
        args = line_arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            class_name = args[0]
            obj_id = args[1]
            obj = storage.session.get(classes[class_name], obj_id)
            if obj:
                storage.session.delete(obj)
                storage.session.commit()
            else:
                print("** no instance found **")
                return
        else:
            print("** Too many argument for destroy **")
            return

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
        args = line_arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            class_name = args[0]
            obj_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            obj = storage.session.get(classes[class_name], obj_id)
            if obj:
                setattr(obj, attribute_name, attribute_value)
                storage.session.commit()
            else:
                print("** no instance found **")
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
        if line_arg:
            args = line_arg.split()
            if len(args) == 1:
                class_name = args[0]
                if class_name not in classes:
                    print("** class doesn't exist **")
                    return
                objs = storage.session.query(classes[class_name]).all()
                for obj in objs:
                    print(obj)
            else:
                print("** Too many argument for all **")
                return
        else:
            for class_name in classes:
                objs = storage.session.query(classes[class_name]).all()
                for obj in objs:
                    print(obj)

    # -------------------------------------------------------------------------

    def default(self, arg):
        """ overides the default method to handle unrecognised commands """
        if arg:
            args = arg.split('.')
            if ('.' in arg and '(' in arg and args[0] in classes
                    and args[1][-1:] == ")"):
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
                    count = storage.session.query(classes[obj_class]).count()
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
            print("** Too many argument **")


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
            print(" executing {} : {}".format(command, e))


if __name__ == '__main__':
    UniConnectCommand().cmdloop()
