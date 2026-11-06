from PIL import Image

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1793950323826_d77a9481.png')
w, h = img.size
y = h // 2

# Find first non-white / non-transparent pixel on the left
left_x = 0
for x in range(w):
    p = img.getpixel((x, y))
    if p[0] < 240 and p[1] < 240:
        left_x = x
        break

right_x = w - 1
for x in range(w - 1, -1, -1):
    p = img.getpixel((x, y))
    if p[0] < 240 and p[1] < 240:
        right_x = x
        break

p_start = img.getpixel((left_x + 5, y))
p_end = img.getpixel((right_x - 5, y))
print(f"Left edge at x={left_x}: {p_start[:3]} -> #{p_start[0]:02x}{p_start[1]:02x}{p_start[2]:02x}")
print(f"Right edge at x={right_x}: {p_end[:3]} -> #{p_end[0]:02x}{p_end[1]:02x}{p_end[2]:02x}")
