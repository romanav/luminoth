import pytest

from TestData.DataSetReader import DataSetReader
from luminoth import Detector, read_image, vis_objects

resources_folder = 'resources'
data_file = "test_data.yaml"


@pytest.fixture
def data_provider():
    return DataSetReader(resources_folder, data_file)


@pytest.fixture
def detector():
    return Detector()


def test_data_read(data_provider, detector):
    for test_image in data_provider:
        image = read_image(test_image.image_path)
        print("Testing image: " + test_image.image_path)
        objects = detector.predict(image)
        assert test_image.expected_data == objects
        print("passed")
