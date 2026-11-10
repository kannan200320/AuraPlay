from PIL import Image
import numpy as np

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1794296479883_af0c1310.jpg')
print("Image dimensions:", img.size)
print("Image mode:", img.mode)

# Let's crop regions to see:
# 1. Background brightness / colors
arr = np.array(img)
print("Mean RGB across image:", arr.mean(axis=(0,1)))
print("Top 100 rows mean RGB:", arr[:100, :, :].mean(axis=(0,1)))
print("Bottom 100 rows mean RGB:", arr[-100:, :, :].mean(axis=(0,1)))
