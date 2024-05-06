import glob

import text_analysis

image_files = [file for file in glob.glob("./dataset/images_ng/*.*")]
ocr_files = [file for file in glob.glob("./dataset/output/merge/*.json")]
image_files.sort()
ocr_files.sort()


count = 0
for i in range(len(image_files)):
    image_file = image_files[i]
    ocr_file = ocr_files[i]

    analysis_result = text_analysis.match(ocr_file)
    if len(analysis_result) > 0:
        print(analysis_result)
        count += 1

print(count, len(ocr_files), count / len(ocr_files))

