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
    EXAM = 'EXAM'

# A Section search map class with a dictionary to store section data
class SectionSearchMap():
    def __init__(self):
        self.search_map = {}

    # This function retreives all the sections using the course name (since names are unique)
    def get_all(self):
        sections = set()
        for item in self.search_map[SearchOptionEnum.NAME]:
            sections.update(self.search_map[SearchOptionEnum.NAME][item])
        return sections

    # This function retrieves a list of sections using the search criteria and the searched item. O(1) to retrieve data
    def search(self, search_by, item):
        if search_by not in self.search_map:
            return set()

        stored_items = self.search_map[search_by]

        return self.search_map[search_by][item] if item in stored_items else set()

    # This function adds a section to the hashmap using the search criteria to store by, the key to use and the item to store
    def add_section(self, store_by, key, section):
        if store_by not in self.search_map:
            self.search_map[store_by] = {}

        if key not in self.search_map[store_by]:
            self.search_map[store_by][key] = set()
        self.search_map[store_by][key].add(section)
