import unittest
from utils import text_node_to_html_node
from textnode import TextNode, TextType

class TestUtils(unittest.TestCase):
    def test_single(self):
        text_node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<b href="https://www.google.com">This is a text node</b>')
    
    def test_multiples(self):
        text_node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        text_node2 = TextNode("This is another text node", TextType.ITALIC, "https://www.google.com")
        html_node2 = text_node_to_html_node(text_node2)
        self.assertEqual(html_node.to_html(), '<b href="https://www.google.com">This is a text node</b>')
        self.assertEqual(html_node2.to_html(), '<i href="https://www.google.com">This is another text node</i>')

    def test_no_url(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<b>This is a text node</b>')
    
    def test_no_text(self):
        text_node = TextNode("", TextType.BOLD, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<b href="https://www.google.com"></b>')
    
    def test_no_text_no_url(self):
        text_node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<b></b>')

    def test_image(self):
        text_node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.google.com" />')

    def test_text(self):
        text_node = TextNode("This is a text node", TextType.TEXT, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), 'This is a text node')

if __name__ == "__main__":
    unittest.main()