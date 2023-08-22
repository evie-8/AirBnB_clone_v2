#!/usr/bin/python3
"""seeing how cmd module works"""


import cmd
import shlex
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class console"""
    prompt = '(hbnb) '
    dicts = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """exit cleanly"""
        return True

    def emptyline(self):
        """Don't do anything"""
        pass

    def do_create(self, line):
        """creating class instances.
         Usage: create <class_name>
            """
        if not line:
            print("** class name missing **")
            return

        token = shlex.split(line)
        if len(token) == 1:
            if token[0] not in HBNBCommand.dicts.keys():
                print("** class doesn't exist **")
                return
            new_obj = HBNBCommand.dicts[token[0]]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """showing object attributes
        Usage: show <class_name> <object_id>
        """
        if not line:
            print("** class name missing **")
            return
        token = shlex.split(line)
        if token[0] not in HBNBCommand.dicts.keys():
            print("** class doesn't exist **")
            return
        if len(token) == 1:
            print("** instance id missing **")
            return
        if len(token) == 2:
            storage.reload()
            objs = storage.all()
            key = token[0] + "." + token[1]
            if key not in objs.keys():
                print("** no instance found **")
            else:
                print(objs[key])

    def do_destroy(self, line):
        """showing object attributes
        Usage: destroy <class_name> <object_id>
        """
        if not line:
            print("** class name missing **")
            return
        token = shlex.split(line)
        if token[0] not in HBNBCommand.dicts.keys():
            print("** class doesn't exist **")
            return
        if len(token) == 1:
            print("** instance id missing **")
            return
        if len(token) == 2:
            storage.reload()
            objs = storage.all()
            key = token[0] + "." + token[1]
            if key not in objs.keys():
                print("** no instance found **")
            else:
                del objs[key]
            storage.save()

    def do_all(self, line):
        """Print all objects
        Usage: all or all <class_name>
        """
        objs = storage.all()
        if not line:
            lists = []
            for k in objs:
                lists.append(str(objs[k]))
            print(lists)
            return
        token = shlex.split(line)
        if len(token) == 1:
            if token[0] not in HBNBCommand.dicts.keys():
                print("** class doesn't exist **")
            else:
                print([str(objs[k]) for k in objs
                      if k.split(".")[0] == token[0]])
                return

    def do_update(self, line):
        """changing attributes or adding attributes
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        if not line:
            print("** class name missing **")
            return
        token = shlex.split(line)
        if token[0] not in HBNBCommand.dicts.keys():
            print("** class doesn't exist **")
            return
        if len(token) == 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs = storage.all()
        key = token[0] + "." + token[1]
        if key not in objs.keys() and len(token) >= 2:
            print("** no instance found **")
            return
        if key in objs.keys() and len(token) == 2:
            print("** attribute name missing **")
            return
        if len(token) == 3:
            print("** value missing **")
            return
        if len(token) == 4:
            if hasattr(objs[key], token[2]):
                attr_type = type(getattr(objs[key], token[2]))
                try:
                    setattr(objs[key], token[2], attr_type(token[3]))
                except ValueError:
                    print("Attribute value doesn't conform to attribute type")
            else:
                val = token[3]
                if val.isdigit() or (
                    val.startswith("-") and val[1:].isdigit()
                ):
                    val = int(val)
                elif self.is_float(val):
                    val = float(val)
                elif isinstance(val, str):
                    val = str(val)
                else:
                    print("value is neither a float, integer nor string")
                setattr(objs[key], token[2], val)
            storage.save()

    def is_float(self, value):
        """check is am a fault"""
        try:
            val = float(value)
            return val.is_integer() is False
        except ValueError:
            return False

    def do_count(self, line):
        """count number of objects of an instance
        <class_name>.count()
        """
        count = 0
        objs = storage.all()
        token = shlex.split(line)
        if len(token) == 1:
            if token[0] in HBNBCommand.dicts.keys():
                for k in objs:
                    if k.split(".")[0] == token[0]:
                        count += 1
                print(count)

    def default(self, line):
        """default commands"""
        commands = {
            "show": self.do_show,
            "all": self.do_all,
            "count": self.do_count,
            "update": self.do_update,
            "destroy": self.do_destroy
            }
        match = re.match(r'(\w+)\.(\w+)\((.*?)\)', line)
        if match:
            class_name = match.group(1)
            command = match.group(2)
            content = match.group(3)
            token = " ".join(content.split(","))
            if command in commands.keys():
                if command == "update":
                    curly_braces = re.search(r"\{(.*?)\}", line)
                    if curly_braces:
                        # print(curly_braces.group())
                        dicts = eval(curly_braces.group())
                        for k, v in dicts.items():
                            ar = content.split(",")[0] + " " + k + " " + str(v)
                            tokens = class_name + " " + ar
                            commands[command](tokens)
                    else:
                        commands[command](class_name + " " + token)
                        return
                lines = class_name + " " + token
                commands[command](lines)
            else:
                print("** Unknown command **")
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
