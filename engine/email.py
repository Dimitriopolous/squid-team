#!/usr/bin/python3
'''
   This module contains the functionality to retrieve and save user names and
   emails/
'''
import email
import json
import smtplib
import uuid


server = smtplib.SMTP('smtp.gmail.com', 587)


class Email():
    '''
       Class definition to store user emails.
    '''
    __file_path = "email.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        ''' This will initiate an email object instance. '''
        self.id = str(uuid.uuid4())
        if "first_name" not in kwargs:
            print("First name required")
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        ''' Serializes __objects to JSON file. '''
        email_dict = {}
        json_dict = self.load()

        for key, value in self.__dict__.items():
            if key == "first_name" or key == "last_name" or key == "email":
                email_dict[key] = value

        json_dict[self.id] = email_dict

        with open(self.__file_path, mode="w", encoding="utf-8") as fp:
            json.dump(json_dict, fp)

    def send(self):
        ''' Sends emails to all users '''
        msg = "Hi!!!!!"
        server.starttls()
        server.login("searchsquid", "squidsquad7")

        email_list = self.load()
        for item in email_list.values():
            send_to = item["email"]
            server.sendmail("searchsquid@gmail.com", send_to, msg)
        server.quit()

    def load(self):
        ''' Loads the email JSON file from storage. '''
        with open("email.json", mode='r+', encoding="utf-8") as fp:
            Email.__objects = json.load(fp)
        return Email.__objects
