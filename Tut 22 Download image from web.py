<<<<<<< HEAD
import random
import urllib.request


def download_image(url):
    name = random.randrange(1, 1000)
    filename = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, filename)  # downloads the image and saves it with fullname.jpg


download_image("https://vignette.wikia.nocookie.net/shipping/images/f/f3/Dean-S13.jpg/revision/latest?cb=20180123071437.jpg")
=======
import random
import urllib.request


def download_image(url):
    name = random.randrange(1, 1000)
    filename = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, filename)  # downloads the image and saves it with fullname.jpg


download_image("https://vignette.wikia.nocookie.net/shipping/images/f/f3/Dean-S13.jpg/revision/latest?cb=20180123071437.jpg")
>>>>>>> 7cbaa6ef51166585a53d61caa11cbe9a1c6e5815
