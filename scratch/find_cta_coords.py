from PIL import Image

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1794294387469_9eacdeb1.png')
w, h = img.size

for card_idx, x_range in enumerate([(0, 315), (315, 630), (630, 945)], 1):
    ys = []
    xs = []
    for y in range(250, h):
        for x in range(x_range[0], x_range[1]):
            r, g, b, *a = img.getpixel((x, y))
            if (b > 180 and g > 150) or (r > 130 and b > 180 and g < 100):
                ys.append(y)
                xs.append(x)
    if ys:
        print(f"Card {card_idx} CTA button: Y=[{min(ys)}, {max(ys)}], height={max(ys)-min(ys)+1}, X=[{min(xs)}, {max(xs)}], width={max(xs)-min(xs)+1}")
