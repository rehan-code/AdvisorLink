# An HTML node containing references to its parent, children, and attributes.
class HTMLNode():
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
        children_string = ' '.join([i if isinstance(i, str) else i.format(None if indentation is None else indentation + 1) for i in self.children])
        attributes_string = (' ' + ' '.join([f'{i}={str(self.attributes[i])}' for i in self.attributes.items()])) if len(self.attributes) > 0 else ''
        indentation = '' if indentation is None else '\n' + ('  ' * indentation)
        if len(self.children) == 0:
            return f'{indentation}<{self.tag}{attributes_string} />'
        return f'{indentation}<{self.tag}{attributes_string}>{children_string}{indentation}</{self.tag}>'

    # Find the first child node with specific tag and attributes
    def find_element(self, tag=None, attr=None, value=None):
        if isinstance(self, str) is False and (not tag or tag == self.tag) and (not attr or (attr in self.attributes and value in self.attributes[attr].split())):
            return self

        for child in self.children:
            if isinstance(child, str) is False:
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
