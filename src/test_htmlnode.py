import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
        print(f"Props to HTML: {node.props_to_html()}")

    def test_leaf_node_initialization(self):
        node = LeafNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click here")
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})
        print(f"Leaf Node Initialization: {node}")

    def test_leaf_node_to_html(self):
        node = LeafNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click here</a>')
        print(f"Leaf Node to HTML: {node.to_html()}")

    def test_leaf_node_to_html_no_value(self):
        node = LeafNode(tag="a", value=None, props={"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node.to_html()
        print(f"Leaf Node to HTML (no value): Raised ValueError as expected")

    def test_parent_node_initialization(self):
        children = [
            LeafNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"}),
            LeafNode(tag="p", value="This is a paragraph.", props={})
        ]
        parent = ParentNode(tag="div", children=children, props={"class": "container"})
        self.assertEqual(parent.tag, "div")
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.props, {"class": "container"})
        print(f"Parent Node Initialization: {parent}")

    def test_parent_node_to_html(self):
        children = [
            LeafNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"}),
            LeafNode(tag="p", value="This is a paragraph.", props={})
        ]
        parent = ParentNode(tag="div", children=children, props={"class": "container"})
        expected_html = '<div class="container"><a href="https://www.google.com" target="_blank">Click here</a><p>This is a paragraph.</p></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_parent_node_no_children(self):
        parent = ParentNode(tag="div", children=[], props={"class": "container"})
        self.assertEqual(parent.tag, "div")
        self.assertEqual(len(parent.children), 0)
        self.assertEqual(parent.props, {"class": "container"})
        expected_html = '<div class="container"></div>'
        self.assertEqual(parent.to_html(), expected_html)
        print(f"Parent Node to HTML (no children): {parent.to_html()}")

    def test_text_node(self):
        node = LeafNode(tag=None, value="Just text", props={})
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Just text")
        self.assertEqual(node.props, {})
        self.assertEqual(node.to_html(), "Just text")
        print(f"Text Node Initialization: {node}")

    def test_self_closing_tag(self):
        #Tests a LeafNode that represents a self-closing tag.
        node = LeafNode(tag="img", value=None, props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, None)
        self.assertEqual(node.props, {"src": "image.png", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="An image" />')
        print(f"Self-Closing Tag Initialization: {node}")

    def test_parent_node_multiple_children(self):
        #Tests a ParentNode with multiple children, including a self-closing tag.
        children = [
            LeafNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"}),
            LeafNode(tag="p", value="This is a paragraph.", props={}),
            LeafNode(tag="img", value=None, props={"src": "image.png", "alt": "An image"})
        ]
        parent = ParentNode(tag="div", children=children, props={"class": "container"})
        expected_html = '<div class="container"><a href="https://www.google.com" target="_blank">Click here</a><p>This is a paragraph.</p><img src="image.png" alt="An image" /></div>'
        self.assertEqual(parent.to_html(), expected_html)

        print(f'Parent Node to HTML (multiple children): {parent.to_html()}')

if __name__ == "__main__":
    unittest.main()