# Generated by Django 4.2.7 on 2023-11-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('reg', models.IntegerField(verbose_name='Register Number')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('Course', models.CharField(max_length=100)),
                ('simage', models.ImageField(upload_to='students_image', verbose_name='students image')),
            ],
        ),
    ]
