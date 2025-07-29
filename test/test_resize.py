from PIL import Image

image = Image.open('D:/dev/Python/impreso/final_123456789123456789_test.png')
new_image = image.resize((396, 283))
new_image.save('test_img.png')

print(image.size) # Output: (1920, 1280)
print(new_image.size) # Output: (400, 400)