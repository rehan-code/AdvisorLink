from html.parser import HTMLParser
from .html_node import HTMLNode

# An array of tags that do not require closing tags in HTML.
HTML_VOID_ELEMENTS = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr"]

# A class to parse HTML into a tree of nodes.
class HTMLNodeParser(HTMLParser):
    def __init__(self):
        self.root_node = HTMLNode('root', None, None)
        self.current_node = self.root_node
        super().__init__()

    def handle_starttag(self, tag, attrs):
        self.current_node = HTMLNode(tag, attrs, self.current_node)

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
