# Generated by Django 2.2.4 on 2019-08-28 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Upload time')),
                ('title', models.CharField(help_text='The title of the post', max_length=255, verbose_name='Title')),
                ('image', models.ImageField(help_text='The image of the post', upload_to='images/', verbose_name='Image')),
                ('owner', models.ForeignKey(help_text='The user which owns the post', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
