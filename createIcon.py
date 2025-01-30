from PIL import Image, ImageDraw

# Create a new image with a white background
size = (256, 256)
img = Image.new('RGB', size, 'white')
draw = ImageDraw.Draw(img)

# Draw a simple design (you can modify this)
draw.rectangle([50, 50, 206, 206], outline='black', width=10)
draw.text((70, 100), "LCSC", fill='black', size=80)
draw.text((70, 140), "2", fill='black', size=40)
draw.text((70, 180), "KiCad", fill='black', size=80)

# Save as ICO
img.save('icon.ico')