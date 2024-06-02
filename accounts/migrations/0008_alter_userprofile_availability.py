# Generated by Django 5.0.4 on 2024-04-28 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_userprofile_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='availability',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')], default='morning', max_length=10),
        ),
    ]