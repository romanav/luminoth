import pytest

from TestData.DataSetReader import DataSetReader, TestImage


@pytest.fixture
def data_reader():
    data_file = "mocs/test_data.json"
    return DataSetReader(data_file)


def test_read_data(data_reader):
    images = data_reader.get_images()
    assert isinstance(images[0], TestImage)
