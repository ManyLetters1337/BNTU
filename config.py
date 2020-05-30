"""
App Config
"""
import os
from flask_uploads import UploadSet, IMAGES

page_size = 10

secret_key = os.urandom(24)

photos = UploadSet('photos', IMAGES)
basic_image_url = 'https://res.cloudinary.com/manyletters/image/upload/v1589568700/015e96e6a653950ded808f5704c0727f.jpg'

STATUSES = {
    'Pending': 'Pending',
    'Active':'Active'
}