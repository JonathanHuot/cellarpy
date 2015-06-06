from PIL import Image
from PIL import ImageOps


def __transpose_exif_orientation(src, dst):
    def get_exif(img):
        from PIL.ExifTags import TAGS
        ret = {}
        info = img._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret

    exif = get_exif(src)
    if 'Orientation' in exif:
        orientation = exif['Orientation']
        if orientation == 1:
            # Nothing
            pass
        elif orientation == 2:
            # Vertical Mirror
            dst = dst.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            # Rotation 180°
            dst = dst.transpose(Image.ROTATE_180)
        elif orientation == 4:
            # Horizontal Mirror
            dst = dst.transpose(Image.FLIP_TOP_BOTTOM)
        elif orientation == 5:
            # Horizontal Mirror + Rotation 90° CCW
            dst = dst.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_90)
        elif orientation == 6:
            # Rotation 270°
            dst = dst.transpose(Image.ROTATE_270)
        elif orientation == 7:
            # Horizontal Mirror + Rotation 270°
            dst = dst.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_270)
        elif orientation == 8:
            # Rotation 90°
            dst = dst.transpose(Image.ROTATE_90)
    return dst


def _transpose_exif_orientation(src, dst):
    try:
        return __transpose_exif_orientation(src, dst)
    except:
        # no exif present, no jpeg?
        return dst


def resize_fixed_size(src, dest, width, height):
    im = Image.open(src)
    if im.size[0] > im.size[1]:
        bg_size = (im.size[0], height)
    else:
        bg_size = (width, im.size[1])
    im.resize(bg_size, Image.ANTIALIAS)
    thumb = ImageOps.fit(image=im, size=(width, height), method=Image.ANTIALIAS)
    thumb = _transpose_exif_orientation(im, thumb)
    thumb.save(dest, "JPEG", quality=80, optimize=True, progressive=True)


def resize_keep_ratio(src, dest, max_width, max_height):
    im = Image.open(src)
    im.thumbnail((max_width, max_height), Image.ANTIALIAS)
    im = _transpose_exif_orientation(im, im)
    im.save(dest, "JPEG", quality=80, optimize=True, progressive=True)
