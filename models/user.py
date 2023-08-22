#!/usr/bin/python3
""" Defines the user class"""


from models.base_model import BaseModel


class User(BaseModel):
    """This represents the user
    Attributes:
        email: the email of the user
        password: the password of the use
        first_name: the user's first name
        last_name: the user's last name
        """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
