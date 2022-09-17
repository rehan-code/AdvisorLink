#!/usr/bin/python3

from html.parser import HTMLParser

# An array of tags that do not require closing tags in HTML.
HTML_VOID_ELEMENTS = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr"]

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

    for row in table_body.children:
        # Only extract information from rows that actually contain course data.
        if (row.child(0) and row.child(0).child(0) and row.child(0).child(0) != 'Sections'):
            row_id = row.child(0).child(0)
            course_name = row.find_element('p', 'id', f'WSS_COURSE_SECTIONS_{row_id}').child(0)
            status = row.find_element('p', 'id', f'LIST_VAR1_{row_id}').child(0)
            title_raw = row.find_element('a', 'id', f'SEC_SHORT_TITLE_{row_id}').child(0)
            location = row.find_element('p', 'id', f'SEC_LOCATION_{row_id}').child(0)
            faculty = row.find_element('p', 'id', f'SEC_FACULTY_INFO_{row_id}').child(0)
            capacity_raw = row.find_element('p', 'id', f'LIST_VAR5_{row_id}').child(0)
            credits = row.find_element('p', 'id', f'SEC_MIN_CRED_{row_id}').child(0)
            level = row.find_element('p', 'id', f'SEC_ACAD_LEVEL_{row_id}').child(0)

            meeting_input = row.find_element('td', 'class', 'SEC_MEETING_INFO').find_element('input')
            meeting_string = meeting_input.attributes["value"]

            # print(course_name, status, title_raw, location, faculty, capacity_raw, credits, level, meeting_string, end='\n\n')

            meeting_data = meeting_string.split()
            print(meeting_data)

if __name__ == "__main__":
    main()
