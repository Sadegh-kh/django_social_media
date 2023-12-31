# Generated by Django 4.2.4 on 2023-09-20 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import social_media.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posted', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, scale=None, size=[300, 300], upload_to=social_media.models.upload_to, verbose_name='عکس')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='social_media.post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='نام کاربری')),
                ('body', models.TextField(verbose_name='متن کامنت')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social_media.post', verbose_name='پست')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'ordering': ['created'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-created'], name='social_medi_created_6d5ea3_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-created'], name='social_medi_created_ae0bed_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-created'], name='social_medi_created_7bd7b8_idx'),
        ),
    ]
