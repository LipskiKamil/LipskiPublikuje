# Generated by Django 4.2.4 on 2024-03-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LipskiPublikuje', '0007_aboutme'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='Fullimage',
            field=models.ImageField(blank=True, null=True, upload_to='fullimages/'),
        ),
    ]