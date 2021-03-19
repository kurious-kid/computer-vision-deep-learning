import cv2
image = cv2.imread("example.png")
print(image.shape)
cv2.imshow("image", image)
cv2.waitKey(0)

# accessing individual pixel value

(b ,g,r) = image[240, 320]
print("pixel value ", (b,g ,r))