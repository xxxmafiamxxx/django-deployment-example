import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_website.settings')
import django
django.setup()
from music.models import Album, Song
import random


from faker import Faker
fakegen = Faker()

albums = ['And death Said Live', 'Blackwater park', 'Orchid', 'Ashes of the Wake', 'Singularity', 'Deliverance', 'Conquering Dystopia']
artist = ['opeth', 'Mors Princepium Est', 'Devil Driver', 'Porcupine tree', 'Belakor', 'Al-Azif']
genre = ['Melodic Death Metal', 'Progressive Death Metal', 'Metal Core']
format = ['mp3']
def album_gen():
    a = Album.objects.get_or_create(album_title=random.choice(albums), artist=random.choice(artist), release_date=fakegen.date(), genre=genre, logo=fakegen.url())[0]
    a.save()
    return a

def generator(N=5):
    for entry in range(N):
        album = album_gen()
        fake_format = format
        fake_song_title = fakegen.name()

        song = Song.objects.get_or_create(album=album, format=fake_format, song_title=fake_song_title)[0]
        song.save()

if __name__ == '__main__':
    print('populating the database')
    generator(100)
    print('populating Complete!')


