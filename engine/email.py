#!/usr/bin/python3
'''
   This module contains the functionality to retrieve and save user names and
   emails/
'''
import email
import json


class Email():
    '''
       Class definition to store user emails.
    '''
    __file_path = "email.json"
    __objects = {}

    def __init__(self, name, email):
        ''' This will initiate an email object instance. '''
        self.name = name
        self.email = email

    def save(self):
        ''' Serializes __objects to JSON file. '''
        objects_dict = {}

    def send(self):
        pass
