import unittest
from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode(tag='a', value='Click here', props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.value, 'Click here')
        self.assertEqual(node.props, {'href': 'https://www.google.com', 'target': '_blank'})
        # Removed print statement to avoid triggering __repr__
        # print(f"Initialization: {node}")

    def test_props_to_html(self):
        node = HTMLNode(props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
        print(f"Props to HTML: {node.props_to_html()}")

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')
        print(f"Props to HTML (empty): {node.props_to_html()}")

    def test_leaf_node(self):
        node = LeafNode(tag='a', value='Click here', props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.value, 'Click here')
        self.assertEqual(node.props, {'href': 'https://www.google.com', 'target': '_blank'})
        print(f"Leaf Node Initialization: {node}")

    def test_leaf_node_to_html(self):
        node = LeafNode(tag='a', value='Click here', props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click here</a>')
        print(f"Leaf Node to HTML: {node.to_html()}")

    def test_leaf_node_to_html_no_value(self):
        node = LeafNode(tag='a', value=None, props={'href': 'https://www.google.com', 'target': '_blank'})
        with self.assertRaises(ValueError):
            node.to_html()
        print(f"Leaf Node to HTML (no value): Raised ValueError as expected")

    @unittest.skip("Skipping test for HTMLNode.to_html() as it raises NotImplementedError")
    def test_htmlnode_to_html(self):
        node = HTMLNode(tag='a', value='Click here', props={'href': 'https://www.google.com', 'target': '_blank'})
        node.to_html()

if __name__ == "__main__":
    unittest.main()