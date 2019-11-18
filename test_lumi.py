from luminoth import Detector, read_image, vis_objects


image = read_image('resources/bikes.jpeg')

# If no checkpoint specified, will assume `accurate` by default. In this case,
# we want to use our traffic checkpoint. The Detector can also take a config
# object.
detector = Detector()

# Returns a dictionary with the detections.
objects = detector.predict(image)

print(objects)

