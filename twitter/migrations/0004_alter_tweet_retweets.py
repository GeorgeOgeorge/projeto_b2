# Generated by Django 4.0.5 on 2022-06-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_alter_tweet_retweets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='retweets',
            field=models.ManyToManyField(blank=True, to='twitter.tweet'),
        ),
    ]
