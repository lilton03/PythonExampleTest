from .ManagerClasses.DownloadManagerClass import DownloadManager


# Download page data
def download_page_data(url):
    # Get DownloadManager
    dl_manager = DownloadManager(url)
    # downloaded_data is the hash name for the data you just downloaded
    data_name = 'downloaded_data'
    dl_manager.download_data(data_name)
    dl_manager.decode_downloaded_data(data_name)

    # Strip some string from the downloaded xml data, in order to successfully format it as an E tree
    dl_manager.strip_downloaded_data_chars('<ImageNetStructure>', data_name)
    dl_manager.strip_downloaded_data_chars('<releaseData>fall2011</releaseData>', data_name)
    dl_manager.strip_downloaded_data_chars('</ImageNetStructure>', data_name)

    # Get Root Pointer of the new E Tree from downloaded_data
    root = dl_manager.get_parse_xml_data(data_name)

    list_data = []
    parent_string = ''
    index = [-1]
    get_tree_data(root, list_data, parent_string, index)
    # Convert List data to string, and save to file, for testing purposes
    #for x in list_data:
        #insert_string += x["name"] + "," + str(x["size"]) + "\n"
    #operation_to_file(insert_string, "downloaded_tree_file.txt", "a")
    return list_data


# Recursive function to extract the downloaded xml tree data
def get_tree_data(node, list_data, parent_string, index):
    # Get Name
    parent_string += node.get('words')
    index[0] += 1
    # Get this node's current index in list_data
    node_index = index[0]
    list_data.insert(index[0], {'name': parent_string, 'size': 0})
    parent_string += '>'
    size = 0
    for child in node:
        size += 1
        size += get_tree_data(child, list_data, parent_string, index)
    # Get the size of the node after counting all of it's children and insert it to list_data
    list_data[node_index]['size'] = size
    return size


# Save a data_string into a specific file
def operation_to_file(data_string, file_name, file_operation):
    file = open(file_name, file_operation)
    file.write(data_string)
    file.close()
