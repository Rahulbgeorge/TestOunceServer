# Generated by Django 2.2 on 2020-07-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.CharField(default=None, max_length=200, null=True)),
                ('file_xxl', models.CharField(default=None, max_length=200, null=True)),
                ('file_xl', models.CharField(default=None, max_length=200, null=True)),
                ('file_l', models.CharField(default=None, max_length=200, null=True)),
                ('icon', models.CharField(default=None, max_length=200, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Not Uploaded'), (2, 'Uploaded'), (3, 'Deleted')], default=1)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Image'), (0, 'Video'), (2, 'Document')])),
            ],
        ),
    ]