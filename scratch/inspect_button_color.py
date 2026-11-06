from PIL import Image

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1793950323826_d77a9481.png')
print("Image size:", img.size)
w, h = img.size

# Sample pixels across the horizontal middle of the button
# The button seems to have text in white, so let's sample non-white pixels near top or bottom quarter
y = h // 4
samples = []
for x in range(w // 6, w * 5 // 6, (w * 4 // 6) // 10):
    p = img.getpixel((x, y))
    samples.append((x, p))

for x, p in samples:
    hex_color = f"#{p[0]:02x}{p[1]:02x}{p[2]:02x}"
    print(f"x={x}: RGB={p[:3]} HEX={hex_color}")
