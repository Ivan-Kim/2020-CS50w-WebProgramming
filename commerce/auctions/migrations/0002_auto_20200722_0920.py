# Generated by Django 3.0.8 on 2020-07-22 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auction',
            name='bid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentedPost', to='auctions.Bid'),
        ),
    ]
