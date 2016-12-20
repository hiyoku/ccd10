
class Image:
    def __init__(self, path, pngname, fitsname, date, hour, getlevel1, getlevel2):
        self.path = path
        self.png_name = pngname
        self.fits_name = fitsname
        self.date = date
        self.hour = hour
        self.getlevel1 = getlevel1
        self.getlevel2 = getlevel2