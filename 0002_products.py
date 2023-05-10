# Generated by Django 4.2.1 on 2023-05-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('productname', models.CharField(max_length=20)),
                ('expirydate', models.DateField()),
            ],
        ),
    ]