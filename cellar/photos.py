from PIL import Image
from PIL import ImageOps


def resize_fixed_size(src, dest, width, height):
    im = Image.open(src)
    if im.size[0] > im.size[1]:
        bg_size = (im.size[0], height)
    else:
        bg_size = (width, im.size[1])
    im.resize(bg_size, Image.ANTIALIAS)
    thumb = ImageOps.fit(image=im, size=(width, height), method=Image.ANTIALIAS)
    thumb.save(dest, "JPEG", quality=80, optimize=True, progressive=True)


def resize_keep_ratio(src, dest, max_width, max_height):
    im = Image.open(src)
    im.thumbnail((max_width, max_height), Image.ANTIALIAS)
    im.save(dest, "JPEG", quality=80, optimize=True, progressive=True)
