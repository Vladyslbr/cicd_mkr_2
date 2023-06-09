# Generated by Django 4.1 on 2023-05-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images')),
                ('created_date', models.DateField()),
                ('age_limit', models.PositiveIntegerField()),
                ('categories', models.ManyToManyField(blank=True, to='gallery.category')),
            ],
        ),
    ]
