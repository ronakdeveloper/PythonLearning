class DataSource:
    def __init__(self, name):
        self.__name = name
    
    def getname(self):
        return self.__name

    def read(self):
        return 'No Data'

class CSVSource(DataSource):
    def __init__(self, name):
        super().__init__(name)

    def read(self):
        return "Reading from CSV"

class APISource(DataSource):
    def __init__(self, name):
        super().__init__(name)

    def read(self):
        return "Reading from API"

arr = [CSVSource('Frontend'), APISource('Backend')]

for row in arr:
    print(row.getname(), '|',row.read())