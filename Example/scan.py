import pytesseract
import cv2

# Load the Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the book image
book_image = cv2.imread('book_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(book_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform OCR on the thresholded image
text = pytesseract.image_to_string(thresh)

# Print the OCR text
print(text)
