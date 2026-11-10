from PIL import Image

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1794294387469_9eacdeb1.png')
print("Image size:", img.size)

# Let's crop into 3 cards
w, h = img.size
card1 = img.crop((0, 0, w//3, h))
card2 = img.crop((w//3, 0, 2*w//3, h))
card3 = img.crop((2*w//3, 0, w, h))

print("Width per card approx:", w//3)
