# Generated by Django 4.2.4 on 2024-03-21 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LipskiPublikuje', '0004_articles_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('CommentContent', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LipskiPublikuje.articles')),
            ],
        ),
    ]
