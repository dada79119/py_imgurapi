from imgurpython import ImgurClient
import random

def imgurget():
    client_id = 'your client id'
    client_secret = 'your client secret'
    album_id = 'your album id'
    client = ImgurClient(client_id, client_secret)
    images = client.get_album_images(album_id)
    index = random.randint(0, len(images) - 1)
    url = images[index].link.replace('http', 'https')
    return url

print(imgurget())

