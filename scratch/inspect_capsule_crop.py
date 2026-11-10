from PIL import Image
import numpy as np

img = Image.open('C:/Users/KANNAN/.gemini/antigravity/brain/eb3d6109-6ab7-4408-bf23-62466738bcae/.user_uploaded/media_1794296479883_af0c1310.jpg')
w, h = img.size

# Let's crop around the capsule:
# In the image (1024 x 278):
# Capsule is roughly in bottom half, centered horizontally:
# x from ~280 to 730, y from ~160 to 230
crop_capsule = img.crop((280, 160, 744, 230))
crop_capsule.save('scratch/capsule_crop.png')

# Let's inspect RGB of capsule border and inside
arr = np.array(crop_capsule)
print("Capsule crop size:", crop_capsule.size)
print("Capsule inner mean RGB:", arr[20:50, 50:-50].mean(axis=(0,1)))
print("Capsule border top row mean RGB:", arr[0:5, 100:300].mean(axis=(0,1)))
