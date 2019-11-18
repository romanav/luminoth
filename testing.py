import datetime

import pytest

from test_lib.DataAbstraction import ImageAnalysisData
from test_lib.DataSetReader import DataSetReader
from luminoth import Detector, read_image, vis_objects
import matplotlib.pyplot as plt

resources_folder = 'resources'
data_file = "test_data.yaml"


@pytest.fixture
def data_provider():
    return DataSetReader(resources_folder, data_file)


@pytest.fixture
def detector():
    return Detector()


def test_run_in_bulk_validations_from_file(data_provider, detector):
    execution_times = []
    execution_names = []

    for test_image in data_provider:
        image = read_image(test_image.image_path)
        print("Testing image: " + test_image.image_path)

        start_time = datetime.datetime.now()
        detected_objects = detector.predict(image)
        recognition_time = (datetime.datetime.now() - start_time).total_seconds()

        execution_names.append(test_image.image_path)
        execution_times.append(recognition_time)

        assert_data_recognized(detected_objects, test_image)

    plot_data_to_file(execution_names, execution_times)


def plot_data_to_file(execution_names, execution_times):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(execution_names, execution_times, color='darkgreen', marker='^')
    plt.savefig('execution_times.png')


def assert_data_recognized(detected_objects, test_image):
    returned_data = ImageAnalysisData(detected_objects)
    for i in returned_data:
        rect = i.get_rectangle()
        expected = test_image.get_expected_data()[rect]
        assert expected == i
