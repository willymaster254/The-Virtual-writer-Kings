# Generated by Django 3.1 on 2020-08-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorrecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=500, null=True)),
                ('pages', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.IntegerField(blank=True, default=0.0, null=True)),
                ('uploads', models.FileField(blank=True, max_length=255, null=True, upload_to='Upload_files/%Y%m%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='VueOrders',
        ),
    ]