import re

class EnterUsername():
    def __init__(self, name):
        self._name=name

    def enterUsername(self):
        return self._name

    def validateUsername(self, name):
        if re.match("^[a-zA-Z0-9_]*$", name):
            print("Valid name")
        else:
            print("Invalid name")

