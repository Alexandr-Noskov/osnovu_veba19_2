# Generated by Django 4.2.4 on 2023-09-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('body', models.CharField(verbose_name='содержимое')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='preview/', verbose_name='изображение')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
