import cv2

# 1. Read and Display an Image
image = cv2.imread('landscape.jpg')  
cv2.imshow('Original Image', image)
cv2.imwrite('output_original.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Print Image Details (Shape, Size)
print("Shape (Height, Width, Channels):", image.shape)
print("Size (Total Pixels):", image.size)
print("Data Type:", image.dtype)

# 3. Convert the Image to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.imwrite('output_grayscale.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Find Color of Pixel at [70, 100]
pixel_color = image[70, 100] 
print("Color at [70,100] (BGR):", pixel_color)

# 5. Modify Pixel at [200, 150] to Red
image[200, 150] = [0, 0, 255] 

# 6. Change Pixel Block [100:300, 150:400] to Green
image[100:300, 150:400] = [0, 255, 0] 

cv2.imshow('Modified Image', image)
cv2.imwrite('output_modified.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Resize Image
resized_image = cv2.resize(image, (300, 300)) 
cv2.imshow('Resized Image', resized_image)
cv2.imwrite('output_resized.jpg', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8. Rotate Image
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

cv2.imshow('Rotated Image', rotated_image)
cv2.imwrite('output_rotated.jpg', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9. Flip Image Horizontally and Vertically
h_flip = cv2.flip(image, 1)
v_flip = cv2.flip(image, 0)

cv2.imshow('Horizontally Flipped', h_flip)
cv2.imwrite('output_hflip.jpg', h_flip)

cv2.imshow('Vertically Flipped', v_flip)
cv2.imwrite('output_vflip.jpg', v_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()
