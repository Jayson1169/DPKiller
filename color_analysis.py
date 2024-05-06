import cv2


def analyze(compos: dict, filename: str) -> dict:
    image = cv2.imread(filename)
    for _, compo in compos.items():
        compo_info = compo["compo_info"]
        coordinates = [
            max(compo_info['row_min'] - 25, 0),
            min(compo_info['row_max'] + 25, image.shape[0] - 1),
            max(compo_info['column_min'] - 50, 0),
            min(compo_info['column_max'] + 50, image.shape[1] - 1)
        ]

        clip = image[coordinates[0]:coordinates[1], coordinates[2]:coordinates[3]]
        clip = cv2.cvtColor(clip, cv2.COLOR_BGR2GRAY)
        histogram = cv2.calcHist([clip], [0], None, [2], [0, 256])
        histogram /= histogram.sum()
        compo['color_analysis'] = {'histogram': [histogram[0][0], histogram[1][0]]}

    return compos
