from PIL import Image
from resizeimage import resizeimage

with Image.open("image.jpg") as img:
    width, height = img.size
    dim = max(width, height)
    img = resizeimage.resize_contain(img, [dim, dim], bg_color=(0, 0, 0, 100))
    img.save("test_image.png", "PNG")
