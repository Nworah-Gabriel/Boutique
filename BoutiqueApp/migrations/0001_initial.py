# Generated by Django 3.2.7 on 2023-09-09 22:20

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('Name', models.CharField(default='Anonymous', max_length=200)),
                ('RoomTitle', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(max_length=200)),
                ('CheckIn', models.CharField(default=datetime.datetime(2023, 9, 9, 23, 20, 11, 735599), max_length=50)),
                ('CheckOut', models.CharField(max_length=50)),
                ('DateSubmitted', models.DateTimeField(default=datetime.datetime(2023, 9, 9, 23, 20, 11, 735599), editable=False)),
                ('SpecialRequest', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Anonymous', max_length=200)),
                ('Email', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=500)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Price', models.CharField(max_length=30)),
                ('Description', models.TextField()),
                ('Star', models.IntegerField()),
                ('Image', models.ImageField(upload_to='upload')),
                ('DatePub', models.DateTimeField(default=datetime.datetime(2023, 9, 9, 23, 20, 11, 736597), editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=300)),
            ],
        ),
    ]
