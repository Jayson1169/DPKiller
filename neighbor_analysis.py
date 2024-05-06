import cv2


def analyze(compos: dict, filename: str) -> dict:
    image = cv2.imread(filename)
    image_size = image.shape[0] * image.shape[1]
    factor = int(image_size * 0.05)
    for compo_id, compo in compos.items():
        compo_info = compo['compo_info']
        coordinates = [
            max(compo_info['row_min'] - factor, 0),
            min(compo_info['row_max'] + factor, image.shape[0] - 1),
            max(compo_info['column_min'] - factor, 0),
            min(compo_info['column_max'] + factor, image.shape[1] - 1)
        ]
        neighbors = find_neighbors(compo_id, compos, coordinates)
        compos[compo_id]['near_analysis'] = {'neighbors': neighbors}

    return compos


def find_neighbors(anchor_id: str, compos: dict, coordinates: list):
    neighbors = []
    for compo_id, compo in compos.items():
        if compo_id == anchor_id:
            continue

        compo_info = compo['compo_info']
        if compo_info['row_min'] < coordinates[0] and compo_info['row_max'] > coordinates[1]:
            continue
        if compo_info['column_min'] < coordinates[2] and compo_info['column_max'] > coordinates[3]:
            continue
        neighbors.append(compo_id)

    return neighbors
