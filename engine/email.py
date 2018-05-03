#!/usr/bin/python3
'''
   This module contains the functionality to retrieve and save user names and
   emails/
'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import json
import PyPDF2
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
        if "first_name" not in kwargs or "last_name" not in kwargs or "email"\
           not in kwargs:
            return True
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
        msg = MIMEMultipart()

        msg["Subject"] = "Hey Friend!"
        msg["From"] = "searchsquid@gmail.com"

        body = "Find the Path of Relationships Between Actors\nEver wonder if two of your favorite actors starred in the same movie?\nSquid Search has your answers!\nWe’re an online search engine that allows users to input the names of two actors and find out how many degrees of separation there are between them through the movies that they’ve acted in. Squid Search can help you discover movies that you might love, follow your favorite star’s creative works, or feed into your curiosity about which actors have worked together."

        server.starttls()
        server.login("searchsquid@gmail.com", 'squidsquad7')
        from_addr = "searchsquid@gmail.com"

        email_list = self.load()
        for item in email_list.values():
            msg["To"] = item["email"]
            msg.attach(MIMEText(body, 'plain'))
            send_to = item["email"]
            server.sendmail("searchsquid@gmail.com", send_to, msg.as_string())
        server.quit()

    def load(self):
        ''' Loads the email JSON file from storage. '''
        with open("email.json", mode='r+', encoding="utf-8") as fp:
            Email.__objects = json.load(fp)
        return Email.__objects
