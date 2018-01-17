from .ManagerClasses.TreeManagerConverterClass import TreeManagerConvert


# get the tree from the list, given the tree's root name
def get_tree_format(list_data, root_name):
    list_name = "temp_list"
    tree_manager_converter = TreeManagerConvert(list_data, list_name)
    tree = tree_manager_converter.get_tree_from_list(list_name, root_name)
    tree = tree.get_properly_formatted_tree(root_name)
    return tree
