from enum import Enum

# An enum with all the search options
class SearchOptionEnum(str, Enum):
    CODE = 'CODE'
    FACULTY = 'FACULTY'
    CREDITS = 'CREDITS'
    INSTRUCTOR = 'INSTRUCTOR'
    BUILDING = 'BUILDING'
    NAME = 'NAME'
    TERM = 'TERM'
    SECTION = 'SECTION'
    LEVEL = 'LEVEL'
    LOCATION = 'LOCATION'
    YEAR = 'YEAR'

# A Section search map class with a dictionary to store section data
class SectionSearchMap():
    def __init__(self):
        self.searchMap = {}

    # This function retrieves a list of sections using the search criteria and the searched item. O(1) to retrieve data
    def search(self, searchBy, item):
        if (searchBy not in self.searchMap):
            return set()

        stored_items = self.searchMap[searchBy]

        return (self.searchMap[searchBy][item] if item in stored_items else set())

    # This function adds a section to the hashmap using the search criteria to store by, the key to use and the item to store
    def add_section(self, storeBy, key, section):
        if storeBy not in self.searchMap: self.searchMap[storeBy] = {}

        if key in self.searchMap[storeBy]:
            self.searchMap[storeBy][key].add(section)
        else:
            self.searchMap[storeBy][key] = set()
            self.searchMap[storeBy][key].add(section)
