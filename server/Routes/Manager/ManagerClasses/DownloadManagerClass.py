import urllib.request
import xml.etree.ElementTree as ET


class DownloadManager:
    def __init__(self, url):
        self.url = url
        self.data = {}
        self.parsed_xml_data = {}

    def download_data(self, data_name):
        self.data[data_name] = urllib.request.urlopen(self.url)

    def decode_downloaded_data(self, data_name):
        self.data[data_name] = self.data[data_name].read()
        self.data[data_name] = self.data[data_name].decode('utf-8')

    def strip_downloaded_data_chars(self, string, data_name):
        self.data[data_name] = self.data[data_name].replace(string, '')

    def get_parse_xml_data(self, data_name):
        self.parsed_xml_data[data_name] = ET.fromstring(self.data[data_name])
        return self.parsed_xml_data[data_name]
