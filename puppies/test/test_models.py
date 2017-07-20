from django.test import TestCase
from ..models import Puppy


class PuppyTest(TestCase):
    """"Test module for Puppy model"""

    def setUp(self):
        Puppy.objects.create(
            name='Perrito', age=3, breed="Salchicha", color="Negro"
        )
        Puppy.objects.create(
            name='Perrote', age=3, breed="Lobezno", color="Blanco"
        )

    def test_puppy_breed(self):
        perrito = Puppy.objects.get(name='Perrito')
        perrote = Puppy.objects.get(name='Perrote')
        self.assertEqual(
            perrito.get_breed(), "Perrito belongs to Salchicha breed."
        )
        self.assertEqual(
            perrote.get_breed(), "Perrote belongs to Lobezno breed."
        )