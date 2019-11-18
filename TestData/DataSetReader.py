import os

import yaml
import json


class TestImage(object):

    def __init__(self, working_folder, image_node):
        self.name = image_node['name']
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
        self._images = None

    def get_images(self):
        if self._images is None:
            with open(os.path.join(self._working_folder, self._data_file_name)) as data_file:
                data = yaml.load(data_file)

            self._images = [TestImage(self._working_folder, i) for i in data['test_data']]

        return self._images

    def __getitem__(self, name):
        for i in self.get_images():
            if i.name == name:
                return i
        raise Exception("Image was not found: " + name)

    def __iter__(self):
        for i in self.get_images():
            yield i
