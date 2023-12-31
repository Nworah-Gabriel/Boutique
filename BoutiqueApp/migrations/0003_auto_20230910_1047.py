# Generated by Django 3.2.7 on 2023-09-10 09:47

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BoutiqueApp', '0002_auto_20230909_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueID', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('Name', models.CharField(default='Anonymous', max_length=200)),
                ('Category', models.CharField(blank=True, choices=[('Women', 'Women'), ('Men', 'Men'), ('Kids', 'Kids')], max_length=50, null=True)),
                ('Price', models.CharField(max_length=50)),
                ('Stock_Number', models.IntegerField()),
                ('Date_Pub', models.DateTimeField(default=datetime.datetime(2023, 9, 10, 10, 47, 15, 958295), editable=False)),
                ('Image', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.AlterField(
            model_name='room',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 10, 47, 15, 958295), editable=False),
        ),
    ]
