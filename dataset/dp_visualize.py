import json
import os

import cv2

input_dir = './images'
dp_dir = './images_with_dp_label'
os.makedirs(dp_dir, exist_ok=True)

annotations = json.load(open('./annotations.json'))
for filename, annotation in annotations.items():
    if len(annotation) == 0:
        continue

    instances = annotation['instances']
    instances = dict(filter(lambda x: x[0].startswith('NG'), instances.items()))
    if len(instances) == 0:
        continue

    image = cv2.imread(os.path.join(input_dir, filename))
    for dp_class, labels in instances.items():
        for label in labels:
            x1, y1, x2, y2 = label['bbox']
            image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 3)

    cv2.imwrite(os.path.join(dp_dir, filename), image)
