import os

import yaml
import json


class TestImage(object):

    def __init__(self, working_folder, image_node):
        self.image_path = os.path.join(working_folder, image_node['image_path'])
        self._expected_file_path = os.path.join(working_folder, image_node['expected'])
        self.expected_data = None

        self._read_expected_data()

    def _read_expected_data(self):
        with open(self._expected_file_path) as f:
            self.expected_data = json.load(f)


class DataSetReader(object):

    def __init__(self, working_folder, data_file_name):
        self._data_file_name = data_file_name
        self._working_folder = working_folder

    def get_images(self):
        with open(os.path.join(self._working_folder, self._data_file_name)) as data_file:
            data = yaml.load(data_file)

        return [TestImage(self._working_folder, i) for i in data['test_data']]
