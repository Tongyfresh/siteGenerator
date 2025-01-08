class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def props_to_html(self):
        # tests if props is empty, if so return empty string, else return the props in the format 'class="container" id="main"'
        if not self.props:
            return ''
        return ' '.join([f'{attribute}="{value}"' for attribute, value in self.props.items()]) # returns the props in the format 'class="container" id="main"'

    def opening_tag(self):
        props_html = self.props_to_html()
        return f'<{self.tag}{" " + props_html if props_html else ""}>' # returns the opening tag with the props in the format '<tag class="container" id="main">'

    def __repr__(self):
        return self.to_html()

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        # checks if the tag is in the self_closing_tags set, if so return the tag with the props and no closing tag, otherwise return the tag with the props and the value and the closing tag '</tag>'
        self_closing_tags = {'img', 'br', 'hr', 'input', 'meta', 'link'}
        if self.tag in self_closing_tags:
            return f'{self.opening_tag()[:-1]} />' # returns the tag with the props and no closing tag. e.g. '<img src="https://www.google.com" />'
        if self.value is None:
            raise ValueError("Value cannot be None")
        if self.tag is None:
            return f'{self.value}'
        return f'{self.opening_tag()}{self.value}</{self.tag}>' # returns the tag with the props and the value and the closing tag '</tag>' e.g. '<a href="https://www.google.com" target="_blank">Click here</a>'

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children is None:
            children = []
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        # returns the opening tag with the props and the children html and the closing tag '</tag>'
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        children_html = ''.join([child.to_html() for child in self.children]) # joins tags of multiple children e.g. '<a href="https://www.google.com" target="_blank">Click here</a><p>This is a paragraph.</p>'
        return f'{self.opening_tag()}{children_html}</{self.tag}>'