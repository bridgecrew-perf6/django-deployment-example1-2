# Generated by Django 2.1.1 on 2022-03-06 07:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='port_folio',
            new_name='portfolio_site',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile',
            new_name='profile_pic',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
