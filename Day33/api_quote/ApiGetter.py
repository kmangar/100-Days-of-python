import requests
from tkinter import *

class ApiGetter:

    def self(self):
        self.quote = ""
        self.api_address = ""

    def get_quote(self):

        response = requests.get(self.api_address)

        response.raise_for_status()

        self.quote = response.json()
        return self.quote