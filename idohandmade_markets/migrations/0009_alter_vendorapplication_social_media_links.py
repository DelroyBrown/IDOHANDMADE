# Generated by Django 5.0.6 on 2024-07-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idohandmade_markets', '0008_alter_marketevent_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorapplication',
            name='social_media_links',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]