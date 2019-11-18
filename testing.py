import pytest
import luminoth

from TestData.DataSetReader import DataSetReader

resources_folder = 'resources'
data_file = "test_data.yaml"


@pytest.fixture
def data_provider():
    return DataSetReader(resources_folder, data_file)


def test_data_read(data_provider):
    images = data_provider.get_images()


