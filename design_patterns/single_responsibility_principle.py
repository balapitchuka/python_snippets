"""
  -- Single Responsibility Principle (SRP)
  -- also known as seperation of concern(SOC)
  

  Defintion:
  A class will have a primary 
  responsibility what it is meant for doing, and it should 
  not have any additional responsibilities.

"""

class Journal(object):
    """Journal class meant for adding entries into journal 
       and removing a particular entry in journal by its position
    """
    def __init__(self):
        self.count = 0
        self.entries = []

    def add_entry(self, entry):
        self.count += 1
        self.entries.append(f"{self.count} : {entry}")
    
    def remove_entry(self, position):
        del self.entries[position]
        print(f"Info : entry at index {position} got deleted ")

    def __str__(self):
        return "\n".join(self.entries)

    # breaking SRP principle
    # def save_to_file(self, filename):
    #    file_obj = open(filename, 'w')
    #    file_obj.write(str(self)) 
    #    file_obj.close()
    #    print(f"Info : Journal saved successfully to the file {filename}")
    
    # def load_from_file(self, filename):
    #     pass
    
    # def load_from_web(self, url):
    #     pass
    

class PersistenceManager(object):

    @staticmethod
    def save_to_file(journal, filename):
        file_obj = open(filename, 'w')
        file_obj.write(str(journal))
        file_obj.close()
        print(f"Info : Journal saved successfully to the file {filename}")


journal = Journal()
journal.add_entry("Weather is bad")
journal.add_entry("Completed running 5km.")
journal.add_entry("Financial amount collected from the concerned person.")

print(journal)
journal.remove_entry(1)

filename = 'journal.txt'
#journal.save_to_file(filename)

PersistenceManager.save_to_file(journal, filename)

#verify file

print("\nInfo :  Contents read from file")
with open(filename, 'r') as file_obj:
    print(file_obj.read())