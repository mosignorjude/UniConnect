#!/usr/bin/python3
"""
Defines the base model of the UniConnect project.
Other classes inherit from this class
"""
import uuid
import datetime
from models import storage


class BaseModel():
    """
    Represents UniConnect Model
    Attributes:
        id (str): unique id for each instance.
        created_at (datetime): datetime an instance was created.
        updated_at (datetime): datetime an instance was updated.
    """

    def __init__(self, *args, **kwargs):
        """initializes new instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        parsed_time = datetime.datetime.fromisoformat(value)
                        setattr(self, key, parsed_time)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns printable representation of the model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attributes <updated_at>
        with current date and time
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/value of __dict__
        of the instance
        """
        attr_dict = self.__dict__.copy()
        attr_dict['__class__'] = self.__class__.__name__
        attr_dict['created_at'] = self.created_at.isoformat()
        attr_dict['updated_at'] = self.updated_at.isoformat()

        return attr_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """ Creates an instance from a dictionary """
        return cls(**obj_dict)
