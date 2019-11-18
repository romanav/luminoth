import yaml


class TestImage(object):

    def __init__(self, image_node):
        self.image_path = image_node['image_path']


class DataSetReader(object):

    def __init__(self, data_file_path):
        with open(data_file_path) as data_file:
            self._data = yaml.load(data_file)

    def get_images(self):
        return [TestImage(i) for i in self._data['test_data']]
