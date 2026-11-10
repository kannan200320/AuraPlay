from PIL import Image

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1794294387469_9eacdeb1.png')

# The button background is cyan-to-purple gradient with bright white text
# Let's find rows where cyan/purple button pixels exist between Y=300 and 400
for card_idx, x_range in enumerate([(0, 315), (315, 630), (630, 945)], 1):
    ys = []
    xs = []
    for y in range(310, 390):
        for x in range(x_range[0], x_range[1]):
            r, g, b, *a = img.getpixel((x, y))
            # gradient button colors: cyan (0, 240, 255) to purple (139, 92, 246)
            if (b > 180 and g > 150) or (r > 120 and b > 200 and g < 120) or (b > 220 and g > 170):
                ys.append(y)
                xs.append(x)
    if ys:
        print(f"Card {card_idx} Button exact: Y=[{min(ys)}, {max(ys)}], X=[{min(xs)}, {max(xs)}]")
