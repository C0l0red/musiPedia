# Generated by Django 3.2.5 on 2021-07-24 14:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('release_date', models.DateField()),
                ('cover', models.URLField()),
                ('ratings', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=80)),
                ('stage_name', models.CharField(max_length=80)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField()),
                ('picture', models.URLField()),
                ('ratings', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
            ],
        ),
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('ratings', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='core.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='core.artist')),
                ('featured_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='core.artist')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='record_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='core.recordlabel'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='core.artist'),
        ),
    ]