from .TreeStructure import Tree


class TreeManagerConvert:
    def __init__(self, data_list, list_name):
        self.lists = {list_name: data_list}

    # Add a list to
    def add_list(self, data_list, list_name):
        self.lists[list_name] = data_list

    # Get Tree Object Format from a list given the root name
    def get_tree_from_list(self, list_name, root_name):
        tree = Tree()
        temp_list = self.lists[list_name]
        for pos in range(0, len(temp_list)):
            if temp_list[pos]['name'] == root_name:
                tree.insert_to_tree(root_name,temp_list[pos]['size'])
                break
        for node in temp_list:
            if root_name == node['name'][0:len(root_name)]:
                tree.insert_to_tree(node['name'],node['size'])
        return tree
