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
    """The FileStorage class handles serialization and deserialization of instances to and from JSON format """
    
        #private class attribute
    
    __file_path = "file.json" #path to json file
    __objects = {} # Dictionary to store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __object that contains all instances """
        
        return FileStorage.__objects

    def new(self, obj):
        """ adds new object to __objects with key <class name>.id """
        
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name. obj.id)
        
        FileStorage.__objects[key] = obj


    def save(self):
        """converting a class instance into a json file/format serialization"""
        
        all_objects = FileStorage.__objects

        obj_dict = {}

        #convert each object to its dictionary representation
        for obj in all_objects.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

            #write the serialized objects in the JSON file
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(obj_dict, file)

    def reload(self):
        """taking back the json file into a class instance deserialization"""
        
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                   obj_dict = json.load(file)

                   for key, value in obj_dict.items():
                       class_name , obj_id = key.split(".")
                       
                       if class_name in globals():
                       cls = eval(class_name)
                       
                       instance = cls(**values) # Create an instance using the dictionary of attributes
                       FileStorage.__objects[key] = instance
                except Exception:
                    pass





