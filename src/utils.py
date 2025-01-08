from htmlnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    # only adds href attribute if URL is provided and self-[closing tag] if it's an image
    props = {}
    if text_node.url:
        if text_node.text_type == TextType.LINK:
            props["href"] = text_node.url
        elif text_node.text_type == TextType.IMAGE:
            props["src"] = text_node.url
        else:
            props["href"] = text_node.url

    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text, props=props)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text, props=props)
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props=props)
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text, props=props)
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value=None, props=props)
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text, props=props)

    return LeafNode(tag=None, value=text_node.text, props=props)