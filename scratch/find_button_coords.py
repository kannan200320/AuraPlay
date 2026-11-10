from PIL import Image

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1794294387469_9eacdeb1.png')
w, h = img.size

# The buttons have cyan/purple gradient (e.g. high blue/cyan or high purple)
# Let's find pixel coordinates in each third where button color is present
for card_idx, x_range in enumerate([(0, 315), (315, 630), (630, 945)], 1):
    ys = []
    for y in range(h):
        for x in range(x_range[0], x_range[1]):
            r, g, b, *a = img.getpixel((x, y))
            # cyan is high g and b (e.g. g>180, b>200), purple is high r and b (e.g. r>140, b>200)
            if (b > 180 and g > 150) or (r > 130 and b > 180 and g < 100):
                ys.append(y)
    if ys:
        print(f"Card {card_idx} button Y: min={min(ys)}, max={max(ys)}, height={max(ys)-min(ys)+1}")
    else:
        print(f"Card {card_idx}: no button pixels found")
