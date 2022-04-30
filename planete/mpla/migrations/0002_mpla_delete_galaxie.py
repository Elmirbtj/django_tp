# Generated by Django 4.0.3 on 2022-04-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mpla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('date_de_decouverte', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='galaxie',
        ),
    ]
