#!/usr/bin/python3
""" This Module defines the FileStorage class that serializes instances to JSON and deserializes JSON to instances """

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """The FileStorage class handles serialization and deserialization of instances to and from JSON format
               Attributes:
                __file_path (str): Path to the JSON file.
                 __objects (dict): Dictionary to store objects by <class name>.id.
    """
    
    __file_path = "file.json" #path to json file
    __objects = {} # Dictionary to store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __object that contains all instances """
        
        return FileStorage.__objects

    def new(self, obj):
        """ adds new object to __objects with key <class name>.id """

        if obj:
            key = f"{obj.__class__.name__}.{obj.id}"
            FileStorage.__objects[key] = obj


    def save(self):
        """converting a class instance into a json file/format serialization"""
        
        obj_dict = {}

        #convert each object to its dictionary representation
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

            #write the serialized objects in the JSON file
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(obj_dict, file, default=str)

    def reload(self):
        """taking back the json file into a class instance deserialization"""
        
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                   obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    class_name , obj_id = key.split(".")
                    if class_name in globals():
                       cls = globals()[class_name] # get class anme from global scope                       
                       instance = cls(**values) # Create an instance using the dictionary of attributes
                       FileStorage.__objects[key] = instance
            except Exception:
                    pass
