import argparse
import imutils
import os
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True, help="path to input image(s)")
ap.add_argument("-o", "--output", type=str, required=True, help="path to output image(s)")
args = vars(ap.parse_args())

if os.path.isfile(args["images"]):
    images = [args["images"].split("/")[-1]]
else:
    images = [f for f in os.listdir(args["images"]) if os.path.isfile(os.path.join(args["images"], f))]

for image in images:
    image_name = image.split(".")[0]
    image_extension = image.split(".")[1]
    image_full_path = os.path.join(args["images"], image)
    image_object = cv2.imread(image_full_path)
    for angle in range(90, 271, 90):
        rotated = imutils.rotate_bound(image_object, angle) # looks like rotate bound will shrink the image a bit
        output_image_name = image_name + "_" + str(angle) + "." + image_extension
        output_image_path = os.path.join(args["output"], output_image_name)
        print(output_image_path)
        cv2.imwrite(output_image_path, rotated)