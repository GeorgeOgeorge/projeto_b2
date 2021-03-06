# Generated by Django 4.0.5 on 2022-07-02 19:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_tweet_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='followers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='follows',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
