# Generated by Django 4.1.1 on 2022-12-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_imageupload_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='imageUpload',
        ),
    ]
