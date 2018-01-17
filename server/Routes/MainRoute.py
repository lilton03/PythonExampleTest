from .Manager import DownloadModule
from .Manager import TreeConverterModule
from .Manager import DatabaseModule
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# * Running on http://127.0.0.1:5000/


# route for resetting everything and doing all required tasks for the test
@app.route('/_reset_everything')
def reset_everything():
    tree_data = DownloadModule.download_page_data('http://www.image-net.org/api/xml/structure_released.xml')
    DatabaseModule.delete_all()
    DatabaseModule.insert(tree_data)
    tree_data = DatabaseModule.select_all()
    tree_data = TreeConverterModule.get_tree_format(tree_data, 'ImageNet 2011 Fall Release')
    return jsonify({'response': tree_data, 'status': 200})


# route for retrieving the tree
@app.route('/_get_page_data')
def page_load():
    tree_data = DatabaseModule.select_all()
    tree_data = TreeConverterModule.get_tree_format(tree_data, 'ImageNet 2011 Fall Release')
    return jsonify({'response': tree_data, 'status': 200})


# route for searching a node in tree
@app.route('/_get_node_data')
def get_node():
    status=200
    tree_data = DatabaseModule.get_node(request.args.get('node_name'), request.args.get('node_size'))
    tree_data = TreeConverterModule.get_tree_format(tree_data, 'ImageNet 2011 Fall Release')
    if not tree_data:
        status=400
    return jsonify({'response': tree_data, 'status': status})


# route for displaying the index page
@app.route('/')
def index_html():
    return render_template('index.html')
