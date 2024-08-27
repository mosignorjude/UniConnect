#!/usr/bin/python3
"""
This file defines the file storage system for the project.
"""
import json
from json.decoder import JSONDecodeError


class FileStorage():
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path: str = "file.json"
    __objects: dict = {}
    models = (
        "BaseModel", "User", "Place",
        "Review", "State", "City",
        "Amenity"
    )

    def __init__(self):
        """ class contructor """
        pass

    def all(self):
        """ Returns __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets the object dictionary """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            # value = obj.to_dict()
            FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes objects to JSON file path """
        # from models.class_module import get_all_class
        json_data = {}
        if FileStorage.__objects:
            for key, obj in FileStorage.__objects.items():
                json_data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(json_data, file)

    def reload(self):
        """ Deserializes the JSON file """

        if FileStorage.__file_path:
            try:
                from models.class_module import (
                    BaseModel, User, Student, Lecturer)
                with open(FileStorage.__file_path, 'r') as file:
                    json_data = file.read()
                dict_from_json = json.loads(json_data)
                for key, obj_dict in dict_from_json.items():
                    obj = eval(obj_dict["__class__"])(
                        **obj_dict)  # get class from its name
                    FileStorage.__objects[key] = obj  # Recreate class
            except (FileNotFoundError, JSONDecodeError):
                pass
        else:
            pass
