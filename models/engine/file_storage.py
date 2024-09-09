#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """ """
    __file_path = "file.json" #private class attribute

    __objects = {}

    def all(self):
        """ """
        return FileStorage.__objects[key] = obj

    def new(self, obj):
        """ adds new attribute to class object """
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name. obj.id)
        
        FileStorage.__objects[key] = obj


    def save(self):
        """converting a class instance into a json file/format serialization"""
        all_objects = FileStorage.__objects

        obj_dict = []

        for obj in all_objects.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(obj_dict, file)

    def reload(self):
        """taking back the json file into a class instance deserialization"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                   obj_dict = json.look(file)
                   for key, value in obj_dict.items():
                       class_name , obj_id = key.split(".")
                       
                       cls = eval(class_name)
                       
                       instance = cls(**values)

                       FileStorage.__objects[key] = instance
                except Exception:
                    pass





