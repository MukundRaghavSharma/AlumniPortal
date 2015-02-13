import os
import sys

from tornado.web import RequestHandler

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  

class AlumniService(RequestHandler):
    def get(self, string):
        self.render(os.path.join('..', 'front_end/alumni_info/') + string)
