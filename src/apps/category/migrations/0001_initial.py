# Generated by Django 5.1.1 on 2024-09-30 03:50

import django.db.models.deletion
import src.apps.category.domain.values_object
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryORM',
            fields=[
                ('basedatafieldorm_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basedatafieldorm')),
                ('category', models.CharField(choices=[('Cloth', 'cloth'), ('Accessory', 'accessory')], default=src.apps.category.domain.values_object.CategoryEnum['Cloth'], max_length=16)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.basedatafieldorm',),
        ),
    ]