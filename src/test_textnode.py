import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(repr(node), "TextNode('This is a text node', bold, 'https://www.google.com')")

    def test_case(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url, "https://www.google.com")

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node.url, "https://www.google.com")

if __name__ == "__main__":
    unittest.main()