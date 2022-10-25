# Generated by Django 4.1.2 on 2022-10-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskUserTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('UserEn', models.CharField(max_length=30)),
                ('UserCn', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'TaskUserType',
                'ordering': ['id'],
            },
        ),
    ]