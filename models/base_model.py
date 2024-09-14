#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Defines all attributes and methods for other objects """
    
    def __init__(self,*args, **kwargs):
        """ Initialization of the base model """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
    def __str__(self):
        """returns an object in a string format """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
 # public instance methods

    def save(self):
        """ update the attribute updated_at withe the current date and time when save is called"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns dictinary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        
        return obj_dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
