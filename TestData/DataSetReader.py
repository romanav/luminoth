import yaml




class TestImage(object):

    def __init__(self):
        pass


class DataSetReader(object):

    def __init__(self, data_file):
        self._data_file = data_file
        with open(data_file) as data_file:
            self._data = yaml.load(data_file)

    def get_images(self):
        return [TestImage()]




