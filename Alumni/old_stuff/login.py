import json
import os
import csv

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.escape import url_escape, json_encode 

import tornado

site_username = "webmaster"
site_password = "inuandi"

class AuthLoginHandler(RequestHandler):
    def get(self):
        try:
            error_message = self.get_argument("errormessage")
        except:
            error_message = ""
        self.render("front_end/login.html", error_message = error_message)

    def check_permission(self, username, password):
        if username == site_username and password == site_password:
                return True
        return False

    def post(self):
        self.username = self.get_argument("username", "")
        self.password = self.get_argument("password", "")
        auth = self.check_permission(self.username, self.password)
        if auth:
            self.set_current_user(self.username)
            self.redirect('/')
        else:
            error_msg = "?error=" + tornado.escape.url_escape("Incorrect Login")
            self.redirect('/login/' + error_msg)

    def set_current_user(self, user):
        if user == site_username:
            self.set_secure_cookie("webmaster", "inuandi")
        else:
            self.clear_cookie("webmaster")

class AuthLogoutHandler(RequestHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/" ))
