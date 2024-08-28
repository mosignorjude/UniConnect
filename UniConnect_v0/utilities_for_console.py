#!/usr/bin/python3

"""
These are functions that power the console class under the hood
They perform the basic task in tasks in the console.
"""
# import datetime
from class_module import (
    BaseModel, User, Lecturer, Student, Course, Enrollment)


def create_object(class_name):
    """ creates an object of class_name
    Args:
        class_name (str): class name of the object to be created.
    Return:
        object of class_name.
    """
    if class_name:
        if class_name == "BaseModel":
            return BaseModel()
        elif class_name == "User":
            return User()
        elif class_name == "Student":
            return Student()
        elif class_name == "Lecturer":
            return Lecturer()
        elif class_name == "Course":
            return Course()
        elif class_name == "Enrollment":
            return Enrollment()
    else:
        return None


def check_class_name(classname, all_object):
    """ Returns True if class name exist in the list
    Args:
        classname (str): class name to search for.
        all_object (FileStorage): List of all existing objects (dictionary)
    Return:
        True if the class name exist otherwise False
    """
    if classname and all_object:
        for key, value in all_object.items():
            if key.startswith(f"{classname}."):
                return True

        return False


def check_object(args, all_objects):
    """ Checks if object exists based on class name and id.
    Args:
        args (str): list of strings of arguments passed to the console.
        all_objects (FileStorage): List of all existing objects (dictionary)
    Return:
        returns True if object exists else False.
    """
    if args and len(args) > 1:
        class_name = args[0]
        obj_id = args[1]
        class_key = f"{class_name}.{obj_id}"
        if class_key in all_objects:
            return True
        else:
            return False


def update_obj_attr(args, all_objects, storage):
    """ Update the attribute of an object
    Args:
        args (list): List of strings of arguments
        all_objects (dict): Dictionary of all existing objects
        storage (FileStorage): Storage object that updates
                                and stores the changes.
    Return:
        int: Returns 0 if the update is successful, 1 otherwise
    """
    if args and len(args) == 4:
        class_name = args[0]
        if class_name.startswith('"'):
            class_name = args[0].replace('"', '')
        obj_id = args[1]
        if obj_id.startswith('"'):
            obj_id = args[1].replace('"', '')
        attr_name = args[2]
        if attr_name.startswith('"'):
            attr_name = args[2].replace('"', '')
        attr_value = args[3]
        if attr_value.startswith('"'):
            attr_value = args[3].replace('"', '')

        class_key = f"{class_name}.{obj_id}"
        if class_key in all_objects.keys():
            obj = all_objects[class_key]
            setattr(obj, attr_name, attr_value)
            obj.save()
            all_objects[class_key] = obj
            storage.__objects = all_objects
            storage.save()
            return 0
        else:
            return 1
    return 1


def extract_attr(string):
    """ extract atrribute """
    content = ""
    start_index = string.find(
        "(") + 1  # Find the opening parenthesis and move one position ahead
    end_index = string.find(")")        # Find the closing parenthesis
    if start_index != -1 and end_index != -1:
        content = string[start_index:end_index]
    return content


def custom_split(arg):
    """
    Splits the argument string into a list, stopping at '{'.
    Uses both space and comma as delimiters.
    """
    result = []
    current = []
    in_dict = False

    for char in arg:
        if char == '{':
            in_dict = True

        if (char == ' ' or char == ',') and not in_dict:
            if current:
                result.append(''.join(current))
                current = []
        else:
            current.append(char)

    if current:
        result.append(''.join(current))

    return result
