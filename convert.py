import cv2

img = cv2.imread('cat03-idle-00.png')

# Make greyscale version
rows, cols, _ = img.shape

br = "cat = ["

for i in range(rows):
    line = "["

    for j in range(cols):
        k = img[i, j]
        if k[0] == 0:
            line = line + "0,"
        else:
            line = line + "1,"

    line = line + "0]"

    br = br + line + ",\n"

print(br + "]")
