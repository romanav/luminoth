class DetectedObject(object):

    def __init__(self, object_json):
        self._object_json = object_json

    def get_type(self):
        return self._object_json['label']

    def get_probability(self):
        return self._object_json['prob']

    def get_rectangle(self):
        return set(self._object_json['bbox'])

    def __eq__(self, other):
        if not self.get_rectangle() == other.get_rectangle():
            return False

        if not self.get_type() == other.get_type():
            return False

        if not self.get_probability() == other.get_probability():
            return False
        return True


class ImageAnalysisData(object):

    def __init__(self, test_data):
        self._test_data = test_data
        self._objects = None

    def detected_object(self):
        if not self._objects:
            self._objects = [DetectedObject(i) for i in self._test_data]
        return self._objects

    def __getitem__(self, item):
        if isinstance(item, int):
            return DetectedObject(self._test_data[item])
        if isinstance(item, set):
            for i in self.detected_object():
                if i.get_rectangle() == item:
                    return i
            raise Exception("Cannot find Object with coordinates: " + item)
