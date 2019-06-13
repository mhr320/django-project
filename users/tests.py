from django.test import TestCase
from django.contrib.auth.models import User
from django.db import models
from .models import Profile
from PIL import Image

class ImageCheck(TestCase):

    def test_image_resize_save(self):

        original_image = Image.open('media/profile_pics/mrCrest.png')

        new_image = Image.open('media/profile_pics/mrCrest.png')

        self.assertIs(original_image.save('media/profile_pics/mrCrest.png'), True)
