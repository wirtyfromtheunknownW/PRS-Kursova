from lxml import etree as ET

# Път до XML файла
xml_file = "xml_project/xml_app/library.xml"

# Namespace-и
namespaces = {
    "fiction": "http://example.com/fiction",
    "nonfiction": "http://example.com/nonfiction"
}


# Четене на XML файла
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return tree, root


# Добавяне на нова книга
def add_book(root, namespace, title, author, year):
    book = ET.Element(f"{{{namespace}}}book")
    title_elem = ET.SubElement(book, f"{{{namespace}}}title")
    title_elem.text = title
    author_elem = ET.SubElement(book, f"{{{namespace}}}author")
    author_elem.text = author
    year_elem = ET.SubElement(book, f"{{{namespace}}}year")
    year_elem.text = year
    root.append(book)


# Запазване на промените
def save_xml(tree, file_path):
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")


if __name__ == "__main__":
    tree, root = parse_xml(xml_file)

    # Добавяне на нова книга във fiction
    add_book(root, namespaces["fiction"], "three body problem", "	Liu Cixin", "2008")

    # Запазване на промените
    save_xml(tree, xml_file)
    print(f"Changes saved to {xml_file}")
