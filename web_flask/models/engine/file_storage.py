#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from os.path import isfile
from models.base_model import BaseModel


class FileStorage:
    """Represent a simple file storage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Set a new object in __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize the __objects to the file storage."""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the file storage to __objects."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = BaseModel
                    if cls_name in globals():
                        cls = globals()[cls_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload method for deserializing the JSON file to objects."""
        self.reload()
