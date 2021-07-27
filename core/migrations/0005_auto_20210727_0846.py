# Generated by Django 3.2.5 on 2021-07-27 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20210727_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='song',
            name='ratings',
        ),
        migrations.CreateModel(
            name='SongRating',
            fields=[
                ('rating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.rating')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.song')),
            ],
            bases=('core.rating',),
        ),
        migrations.CreateModel(
            name='ArtistRating',
            fields=[
                ('rating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.rating')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.artist')),
            ],
            bases=('core.rating',),
        ),
        migrations.CreateModel(
            name='AlbumRating',
            fields=[
                ('rating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.rating')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.album')),
            ],
            bases=('core.rating',),
        ),
    ]
