from textnode import TextNode, TextType
from htmlnode import LeafNode
from utils import text_node_to_html_node

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
    html_node = text_node_to_html_node(text_node)
    print(html_node.to_html())

if __name__ == "__main__":
    main()