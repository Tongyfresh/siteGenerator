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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None")
        if self.tag is None:
            return f'{self.value}'
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'