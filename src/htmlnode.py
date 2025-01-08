class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return ' '.join([f'{attribute}="{value}"' for attribute, value in self.props.items()])

    def __repr__(self):
        return self.to_html()