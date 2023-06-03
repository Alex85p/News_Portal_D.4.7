# Generated by Django 4.1.7 on 2023-06-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_rename_text_en_post_text_en_us_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='category name', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(help_text='category name', max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='category name', max_length=32, null=True, unique=True),
        ),
    ]