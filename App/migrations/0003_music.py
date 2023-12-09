# Generated by Django 4.2.7 on 2023-11-14 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=100)),
                ('song_description', models.TextField()),
                ('song_link_youtube', models.TextField()),
            ],
        ),
    ]
