import code128
import io
from PIL import Image, ImageDraw, ImageFont

barcode_param = '9991252930594'
barcode_text = '9991252930594'

# original image
barcode_image = code128.image(barcode_param, height=100)

# empty image for code and text - it needs margins for text
w, h = barcode_image.size
margin = 20
new_h = h +(2*margin) 

new_image = Image.new( 'RGB', (w, new_h), (255, 255, 255))

# put barcode on new image
new_image.paste(barcode_image, (0, margin))

# object to draw text
draw = ImageDraw.Draw(new_image)

# draw text
#fnt = ImageFont.truetype("arial.ttf", 40)
#draw.text( (10, new_h - 10), barcode_text, fill=(0, 0, 0))#, font=fnt)  # 

# save in file 
new_image.save('barcode_image.png', 'PNG')

# show in default viewer
import webbrowser
webbrowser.open('barcode_image.png')

# --- later send it---

barcode_bytes = io.BytesIO()
new_image.save(barcode_bytes, "PNG")
barcode_bytes.seek(0)
data = barcode_bytes.getvalue()