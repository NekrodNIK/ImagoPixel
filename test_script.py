from PIL import Image, ImageFilter, ImageEnhance

image: Image.Image = Image.open("test_image.jpg")
image = image.quantize(colors=5).convert("RGB")

enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(5)
image = image.filter(ImageFilter.GaussianBlur(3))

image = image.filter(ImageFilter.EDGE_ENHANCE)

s = image.size
image = image.resize(size=(64, 64), resample=Image.NEAREST)

image = image.resize(s, resample=Image.NEAREST)


image.save("output.jpg")
