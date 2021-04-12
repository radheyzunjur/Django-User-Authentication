# Generated by Django 2.0.10 on 2019-01-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'account',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
