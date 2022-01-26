# SRP or SOC
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def addEntry(self,text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def removeEntry(self, pos):
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self):
    #     pass

    # def load_from_web(self):
    #     pass

class PersistenceManager:
    @staticmethod
    def save(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.addEntry("I have breakfast today, it was good!")
j.addEntry("I have cried today")
j.addEntry("Tomorrow will be a good day!")

print(str(j))

j.removeEntry(1)

print(str(j))

fname = "journal.txt"
PersistenceManager.save(j, fname)