# Generated by Django 3.1.3 on 2020-11-19 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.sellerstatus'),
        ),
        migrations.AlterField(
            model_name='sellerstatus',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]