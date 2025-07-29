import cv2
imagen1 = cv2.imread('123456789123456789.png')
imagen2 = cv2.imread('123456789123456789.png')
concat_vertical = cv2.hconcat([imagen1, imagen1,imagen1])
cv2.imwrite('opencv_vconcat.png', concat_vertical)
# cv2.imshow('concat_vertical', concat_vertical)



cv2.waitKey(0)
cv2.destroyAllWindows()