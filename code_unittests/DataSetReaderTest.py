import pytest

from test_lib.DataAbstraction import DetectedObject, ImageAnalysisData
from test_lib.DataSetReader import DataSetReader, TestImage


@pytest.fixture
def data_reader():
    return DataSetReader("mocs", "test_data.yaml")


def test_read_image_path(data_reader):
    images = data_reader.get_images()
    assert isinstance(images[0], TestImage)

    assert images[0].image_path == 'mocs/bikes.jpg'
    assert images[1].image_path == 'mocs/people.jpg'


def test_get_by_name(data_reader):
    assert data_reader.get_images()[0] == data_reader['bikes_1']


def test_read_image_path(data_reader):
    image = data_reader['bikes_1']
    analysis = image.get_expected_data()
    objects = analysis.detected_object()
    assert len(objects) == 8


def test_need_to_get_by_array_number(data_reader):
    image = data_reader['bikes_1']
    analysis = image.get_expected_data()
    assert isinstance(analysis[1], DetectedObject)

    assert analysis[1].get_type() == 'bicycle'
    assert analysis[1].get_probability() == 0.9958
    assert analysis[1].get_rectangle() == {6.0, 38.0, 230.0, 155.0}


def test_get_item_by_coordinates():
    obj = get_specific_detected_object_by_coordinates()
    assert isinstance(obj, DetectedObject)
    assert obj.get_probability() == 0.9958
    assert obj.get_type() == 'bicycle'


def test_compare_2_detected_objects():
    obj1 = get_specific_detected_object_by_coordinates()
    obj2 = get_specific_detected_object_by_coordinates()
    assert obj1 == obj2


def get_specific_detected_object_by_coordinates():
    dr1 = DataSetReader("mocs", "test_data.yaml")
    data_abstraction = dr1.get_images()[0].get_expected_data()
    assert isinstance(data_abstraction, ImageAnalysisData)
    obj = data_abstraction[{6.0, 38.0, 230.0, 155.0}]
    return obj
