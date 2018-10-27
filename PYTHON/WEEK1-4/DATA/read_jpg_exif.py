#pip install Pillow

from PIL import Image
from PIL.ExifTags import TAGS
def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    ret = {}
    try:
        img = Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print('IOERROR ' + fname)
    return ret

if __name__ == '__main__':
    fileName = './yourpicname.jpg'
    exif = get_exif_data(fileName)
    print(exif)
    
import piexif
from PIL import Image

img = Image.open('libaray.jpg')
exif_dict = piexif.load(img.info['exif'])
exif_dict
altitude = exif_dict['0th'][306]
b'2018:10:27 22:14:36'
exif_dict['0th'][306] = b'2018:10:27 22:14:36'
exif_bytes = piexif.dump(exif_dict)
img.save('_%s' % fname, "jpeg", exif=exif_bytes)
