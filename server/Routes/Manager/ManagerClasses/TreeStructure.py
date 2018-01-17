class Tree:
    def __init__(self):
        self.tree = {}

    # Get a nodes unique identifier from it's name
    @staticmethod
    def string_hash_function(string_data):
        ret = 0
        for x in range(0, len(string_data)):
            ret += (x + 1) * ord(string_data[x])
        return format(ret, 'X')

    # Traverse through the tree and inserting the new node
    @staticmethod
    def traverses_to_insert_tree(node, node_strings, index,node_size):
        if index < len(node_strings):
            node_hash = Tree.string_hash_function(node_strings[index])
            if node_hash not in node:
                node[node_hash] = {'name': node_strings[index], 'size': 1, 'children': {}}
            if index ==len(node_strings)-1:
                node[node_hash]['size']=node_size
            Tree.traverses_to_insert_tree(node[node_hash]['children'], node_strings, index + 1,node_size)


    # Traverse through the tree and get each node data
    @staticmethod
    def traverse_to_get_data_from_tree(tree, tree_container):
        tree_container['name'] = tree['name']
        tree_container['size'] = tree['size']
        tree_container['children'] = []
        for key in tree['children']:
            tree_container['children'].append({})
            Tree.traverse_to_get_data_from_tree(tree['children'][key],
                                                tree_container['children'][len(tree_container['children']) - 1])

    # Insert new node into tree
    def insert_to_tree(self, node_identifier,node_size):
        node_identifier = node_identifier.split('>')
        self.traverses_to_insert_tree(self.tree, node_identifier, 0,node_size)

    # Get the proper format of the tree based on the test instructions
    def get_properly_formatted_tree(self, root_level_root_name):
        formatted_tree = {}
        if self.string_hash_function(root_level_root_name) in self.tree:
            self.traverse_to_get_data_from_tree(self.tree[self.string_hash_function(root_level_root_name)],
                                                formatted_tree)
        return formatted_tree
