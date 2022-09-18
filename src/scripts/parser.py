#!/usr/bin/python3

from html.parser import HTMLParser
import json 
import re

# An array of tags that do not require closing tags in HTML.
HTML_VOID_ELEMENTS = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr"]

# An array of valid days for class meetings
VALID_DAYS = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']

# A dictionary of values to find and replace to sanitize meeting data
REPLACEMENT_TABLE = {
    'Distance Education': 'DE', 
    'Independent Study': 'IS', 
    'Days TBA Days TBA': 'NoDays', 
    'Times TBA Times TBA': 'NoTimes, ', 
    'Room TBA Room TBA': 'NoRoom', 
    'NoTimes,,': 'NoTimes, ', 
    'NoTimes, ,': 'NoTimes,'
}

# An HTML node containing references to its parent, children, and attributes.
class Node():
    # Creates a node instance given the tag, attributes, and parent node.
    def __init__(self, tag, attributes, parent = None):
        self.tag = tag
        self.parent = parent
        self.children = []
        self.data = ''

        self.attributes = {}
        if attributes:
            for attr, value in attributes:
                self.attributes[attr] = value

        if parent:
            parent.children.append(self)

    # Format the node object into html string
    def format(self, indentation = None):
        children_string = ' '.join([i if isinstance(i, str) else i.format(None if indentation == None else indentation + 1) for i in self.children])
        attributes_string = (' ' + ' '.join([f'{i}={str(self.attributes[i])}' for i in self.attributes])) if len(self.attributes) > 0 else ''
        indentation = '' if indentation == None else '\n' + ('  ' * indentation)
        if len(self.children) == 0:
            return f'{indentation}<{self.tag}{attributes_string} />'
        return f'{indentation}<{self.tag}{attributes_string}>{children_string}{indentation}</{self.tag}>'

    # Find the first child node with specific tag and attributes
    def find_element(self, tag=None, attr=None, value=None):
        if isinstance(self, str) == False and (not tag or tag == self.tag) and (not attr or (attr in self.attributes and value in self.attributes[attr].split())):
            return self

        for child in self.children:
            if isinstance(child, str) == False:
                result = child.find_element(tag, attr, value)
                if result:
                    return result

        return None

    # Returns the ith child of the node if it exists, else None.
    def child(self, index):
        if len(self.children) <= index:
            return None
        return self.children[index]

    # Returns a string representaiton of the node.
    def __str__(self):
        return self.format()

# A class to parse HTML into a tree of nodes.
class NodeHTMLParser(HTMLParser):
    def __init__(self):
        self.root_node = Node('root', None, None)
        self.current_node = self.root_node
        super().__init__()

    def handle_starttag(self, tag, attrs):
        self.current_node = Node(tag, attrs, self.current_node)

        # If the tag closes without a closing tag, invoke the closing behaviour.
        if tag in HTML_VOID_ELEMENTS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag != self.current_node.tag:
            raise Exception(f'Mismatched tag error: Encountered closing tag "{tag}" while in tag {self.current_node.tag}')

        self.current_node = self.current_node.parent

    def handle_data(self, data):
        # Reduce all whitespace to be single spaces.
        simplified_data = " ".join(data.split())
        if len(simplified_data) == 0:
            return

        # If the current data is a string and the previous data received was a string, combine them.
        if (len(self.current_node.children) > 0 and isinstance(self.current_node.children[-1], str)):
            self.current_node.children[-1] = self.current_node.children[-1] + " " + simplified_data
        # Previous data was not a string, so add a new string to the end of the current node's children.
        else:
            self.current_node.children.append(simplified_data)

    def get_root(self):
        return self.root_node

def parse_html(fileName):
    parser = NodeHTMLParser()
    with open(fileName) as fp:
        parser.feed(fp.read())
    return parser.get_root()

def main():
    root = parse_html('courses.html')
    table_body = root.find_element('table', 'summary', 'Sections').child(0)

    course_table = {}

    for row in table_body.children:
        # Only extract information from rows that actually contain course data.
        if (row.child(0) and row.child(0).child(0) and row.child(0).child(0) != 'Sections'):
            row_id = row.child(0).child(0)
            term = row.find_element('p', 'id', f'WSS_COURSE_SECTIONS_{row_id}').child(0)
            status = row.find_element('p', 'id', f'LIST_VAR1_{row_id}').child(0)
            title_raw = row.find_element('a', 'id', f'SEC_SHORT_TITLE_{row_id}').child(0)
            location = row.find_element('p', 'id', f'SEC_LOCATION_{row_id}').child(0)
            instructor = row.find_element('p', 'id', f'SEC_FACULTY_INFO_{row_id}').child(0)
            capacity_raw = row.find_element('p', 'id', f'LIST_VAR5_{row_id}').child(0)
            credits = row.find_element('p', 'id', f'SEC_MIN_CRED_{row_id}').child(0)
            level = row.find_element('p', 'id', f'SEC_ACAD_LEVEL_{row_id}').child(0)

            meeting_input = row.find_element('td', 'class', 'SEC_MEETING_INFO').find_element('input')
            meeting_string = meeting_input.attributes["value"]

            # format meeting string
            for key, value in REPLACEMENT_TABLE.items():
                meeting_string = meeting_string.replace(key, value)
            
            # additional course title parsing
            title_tokens = title_raw.split()

            # handle invalid course entries
            if len(title_tokens) <= 1:
                continue
            
            name = " ".join(title_tokens[2:])
            course_code = "*".join(title_tokens[0].split('*')[:2])

            # additional course section parsing
            total_capacity = 0
            enrolled = 0
            if capacity_raw:
                capacity_tokens = capacity_raw.split('/')
                total_capacity = capacity_tokens[1].replace(' ', '')
                enrolled = capacity_tokens[0].replace(' ', '')

            # additional section meeting parsing
            meetings = []
            meeting_string_tokens = meeting_string.split('\n')

            # create list of meetings for each section
            for meeting in meeting_string_tokens:
                meeting_info_tokens = meeting.split()

                # handle invalid meeting entries
                if len(meeting_info_tokens) <= 1:
                    continue

                section_meeting = {}
                section_meeting['type'] = meeting_info_tokens[1]
                section_meeting['date'] = None
                section_meeting['start_date'] = meeting_info_tokens[0].split('-')[0]
                section_meeting['end_date'] = meeting_info_tokens[0].split('-')[1]

                if meeting_info_tokens[1] == 'EXAM':
                    section_meeting['date'] = meeting_info_tokens[0].split('-')[0]
                    section_meeting['start_date'] = None
                    section_meeting['end_date'] = None
                elif meeting_info_tokens[1] == 'IS':
                    section_meeting['type'] = 'Independent Study'
                elif meeting_info_tokens[1] == 'DE':
                    section_meeting['type'] = "Distance Education"
                    section_meeting['start_time'] = None
                    section_meeting['end_time'] = None
                    section_meeting['building'] = None
                    section_meeting['room'] = None
                    meetings.append(section_meeting)
                    continue

                # retrieve meeting days
                days = []
                for item in meeting_info_tokens:
                    day = item.replace(',','')
                    if day in VALID_DAYS:
                        days.append(day)
                section_meeting['days'] = days

                if 'NoTimes,' in meeting_info_tokens:
                    section_meeting['start_time'] = None
                    section_meeting['end_time'] = None
                else:
                    time_regex = re.compile('([0-9]|0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])\s*([AaPp][Mm])')
                    meeting_times = [item for item in meeting_info_tokens if time_regex.match(item)]
                    section_meeting['start_time'] = meeting_times[0]
                    section_meeting['end_time'] = meeting_times[1].replace(',','')

                if 'NoRoom' in meeting_info_tokens:
                    section_meeting['building'] = None
                    section_meeting['room'] = None
                else:
                    section_meeting['building'] = meeting_info_tokens[-3].replace(',','')
                    section_meeting['room'] = meeting_info_tokens[-1]

                meetings.append(section_meeting)

            section = {}
            section['term'] = term
            section['number'] = title_tokens[0].split('*')[2]
            section['location'] = location
            section['instructor'] = instructor
            section['capacity'] = total_capacity
            section['enrolled'] = enrolled
            section['status'] = status
            section['meetings'] = meetings

            # insert section in existing course entry
            if course_code in course_table:
                existing_course = course_table.get(course_code)
                existing_course['sections'].append(section)
                continue
            
            course = {}
            course['name'] = name
            course['faculty'] = title_tokens[0].split('*')[0]
            course['course_code'] = course_code.split('*')[1]
            course['credits'] = credits
            course['level'] = level
            course['sections'] = [section]
            course_table[course_code] = course

    output = {'courses': list(course_table.values())}

    with open('courses.json', 'w') as fp:
        json.dump(output, fp, ensure_ascii=False, indent=2)
        

if __name__ == "__main__":
    main()
