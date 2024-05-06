def analyze(compos: dict) -> dict:
    for compo_id, compo in compos.items():
        compo_info = compo['compo_info']
        max_height = compo_info['height']
        max_width = compo_info['width']
        for neighbor in compo['near_analysis']['neighbors']:
            neighbor_info = compos[neighbor]['compo_info']
            max_height = max(max_height, neighbor_info['height'])
            max_width = max(max_width, neighbor_info['width'])

        compo['size_analysis'] = {'relative_height': compo_info['height'] / max_height,
                                    'relative_width': compo_info['width'] / max_width}
    return compos
