#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        newDict = {}
        print("hi")
        if cls:
            for key, value in self.__objects.items():
                if value.__class__ == cls:
                    newDict[key] = value
            return newDict
        return FileStorage.__objects
        # newDict = {}
        # if cls:
        #     class_name = cls().__class__.__name__
        #     for key, value in FileStorage.__objects.items():
        #         if key[:5] == class_name:
        #             newDict[key] = value
        #     return newDict
        # return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        to delete obj from __objects
        """
        from models.__init__ import storage
        if obj is None:
            return
        instance = f"{obj.__class__.__name__}.{obj.id}"

        if instance in FileStorage.__objects.keys():
            del FileStorage.__objects[instance]
        storage.save()

    