# Generated by Django 5.1.1 on 2024-09-30 03:50

import django.db.models.deletion
import src.apps.product.domain.values_object
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductORM',
            fields=[
                ('basedatafieldorm_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basedatafieldorm')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Unisex', 'unisex')], default=src.apps.product.domain.values_object.GenderEnum['Unisex'], max_length=16)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_brand', to='base.basedatafieldorm')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.categoryorm')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_color', to='base.basedatafieldorm')),
                ('place_sell', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_place_sell', to='base.basedatafieldorm')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_size', to='base.basedatafieldorm')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.basedatafieldorm', models.Model),
        ),
    ]