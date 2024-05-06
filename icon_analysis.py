import cv2


def match(image_filename: str, template_filename: str):
    image = cv2.imread(image_filename)
    template = cv2.imread(template_filename)
    template_height, template_width = template.shape[:2]
    methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF_NORMED]
    for method in methods:
        result = cv2.matchTemplate(image, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        left_top = min_loc if method == cv2.TM_SQDIFF_NORMED else max_loc
        right_bottom = (left_top[0] + template_width, left_top[1] + template_height)  # 矩形框右下角坐标
        image = cv2.rectangle(image, left_top, right_bottom, (0, 0, 255), 2)  # 在target图像上绘制匹配的矩形框
        cv2.imshow('match-' + str(method), image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


match('./dataset/images_ng/12.jpg', './adchoice.jpg')
