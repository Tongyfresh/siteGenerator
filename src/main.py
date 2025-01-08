from textnode import *

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
    print(text_node)

if __name__ == "__main__":
    main()