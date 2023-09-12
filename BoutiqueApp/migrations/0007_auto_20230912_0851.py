# Generated by Django 3.2.7 on 2023-09-12 07:51

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BoutiqueApp', '0006_auto_20230912_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Date_Pub',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 12, 8, 51, 4, 331806), editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='uniqueID',
            field=models.UUIDField(blank=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.CharField(blank=True, choices=[('Kids', 'Kids'), ('Women', 'Women'), ('Men', 'Men')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Date_Pub',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 8, 51, 4, 330806), editable=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 8, 51, 4, 331806), editable=False),
        ),
    ]
