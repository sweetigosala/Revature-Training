class College:
    def __init__(self,ColCode,ColName):
        self._ColCode = ColCode
        self._ColName = ColName

    @property
    def ColCode(self):
        return self._ColCode

    @property
    def ColName(self):
        return self._ColName

    def display(self):
        return self._ColCode, self._ColName


