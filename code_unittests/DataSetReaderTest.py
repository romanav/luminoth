import pytest

from TestData.DataSetReader import DataSetReader, TestImage


@pytest.fixture
def data_reader():
    return DataSetReader("mocs", "test_data.yaml")


def test_read_image_path(data_reader):
    images = data_reader.get_images()
    assert isinstance(images[0], TestImage)

    assert images[0].image_path == 'mocs/bikes.jpg'
    assert images[1].image_path == 'mocs/people.jpg'


def test_read_image_date(data_reader):
    images = data_reader.get_images()
    assert isinstance(images[0].expected_data, list)
