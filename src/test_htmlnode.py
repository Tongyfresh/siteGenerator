import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_initialization(self):
        node = HTMLNode(tag='a', value='Click here', props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.value, 'Click here')
        self.assertEqual(node.props, {'href': 'https://www.google.com', 'target': '_blank'})

    def test_props_to_html(self):
        node = HTMLNode(props={'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')
    
    

if __name__ == "__main__":
    unittest.main()