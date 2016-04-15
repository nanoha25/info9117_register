class EnterPassword():
    def __init__(self, psin):
        self._psin = psin

    def enterPassword(self):
        return self._psin

    def validatePassword(self, psin):
        if psin.isdigit():
            print("Weak")
        else:
            print("Good")
