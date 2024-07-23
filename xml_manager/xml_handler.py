import xml.etree.ElementTree as ET
import os


class XMLHandler:
    def __init__(self, file):
        self.file = file
        self.tree = None

    def load(self):
        self.tree = ET.parse(f'./files/{self.file}')
        return self.tree

    def print(self):
        if self.tree is None:
            self.load()
        print(ET.tostring(self.tree.getroot(), encoding='utf8').decode('utf8'))

    def save(self, output, data):
        if self.tree is None:
            self.load()

        root = self.tree.getroot()
        item_tag = root[0].tag  # Get the tag name for each item
        data_tags = [elem.tag for elem in root[0]]  # Get the tag names for each sub-element in the items

        new_root = ET.Element(root.tag)

        for row in data:
            item = ET.SubElement(new_root, item_tag)
            for value, tag in zip(row, data_tags):
                item_data = ET.SubElement(item, tag)
                item_data.text = str(value)

        if not os.path.isdir("./output"):
            os.mkdir("./output")

        new_tree = ET.ElementTree(new_root)
        new_tree.write(f'./output/{output}', encoding='utf-8', xml_declaration=True)

    def read(self):
        if self.tree is None:
            self.load()

        root = self.tree.getroot()
        header_columns = set()
        data = [""]
        for row in root:
            data_to_add = []
            for column in row:
                header_columns.add(column.tag)
                data[0] = list(header_columns)
                data_to_add.append(column.text)
            data.append(data_to_add)
        return data
