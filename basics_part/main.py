import cv2
import warnings

# Ignore warnings for simplicity
warnings.filterwarnings('ignore')

# Read the image
image_path = './img/khabin.jpg'
image = cv2.imread(image_path)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Get the size of the image
image_size = image.shape
print(f'The size of the image: {image_size}')
print(f'The height of the image: {image_size[0]}')
print(f'The width of the image: {image_size[1]}')

# Crop a region of interest (ROI) from the image
x, y, w, h = 100, 50, 200, 150
cropped_image = image[y:y+h, x:x+w]
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)

# Convert the image to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)

# Apply Gaussian Blur to the image
blur = cv2.GaussianBlur(image, (7, 7), cv2.BORDER_DEFAULT)
cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)

# Apply Canny edge detection
canny = cv2.Canny(image, 125, 175)
cv2.imshow('Canny Edge Detection', canny)
cv2.waitKey(0)

# Resize the image
width, height = int(image_size[1] * 1.5), image_size[0]
size = (width, height)
resized = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
