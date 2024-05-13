# Generated by Django 5.0.6 on 2024-05-12 16:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCateringType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_kitchen', models.BooleanField(default=True)),
                ('kitchen_area', models.FloatField()),
                ('hall_area', models.FloatField()),
                ('seating_capacity', models.IntegerField()),
                ('has_delivery', models.BooleanField()),
                ('opening_hours', models.TimeField()),
                ('number_of_employees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BaseRetailCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_area', models.FloatField()),
                ('warehouse_area', models.FloatField()),
                ('opening_hours', models.TimeField()),
                ('number_of_employees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BaseServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_office', models.BooleanField()),
                ('office_area', models.FloatField()),
                ('opening_hours', models.TimeField()),
                ('number_of_employees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_type', models.CharField(choices=[('catering', 'Catering'), ('retail', 'Retail'), ('service', 'Service')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BurgerJoint',
            fields=[
                ('basecateringtype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.basecateringtype')),
            ],
            bases=('main.basecateringtype',),
        ),
        migrations.CreateModel(
            name='CoffeeHouse',
            fields=[
                ('basecateringtype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.basecateringtype')),
            ],
            bases=('main.basecateringtype',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('basecateringtype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.basecateringtype')),
            ],
            bases=('main.basecateringtype',),
        ),
        migrations.CreateModel(
            name='BooksRetail',
            fields=[
                ('baseretailcategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseretailcategory')),
            ],
            bases=('main.baseretailcategory',),
        ),
        migrations.CreateModel(
            name='ClothesRetail',
            fields=[
                ('baseretailcategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseretailcategory')),
            ],
            bases=('main.baseretailcategory',),
        ),
        migrations.CreateModel(
            name='SportRetail',
            fields=[
                ('baseretailcategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseretailcategory')),
            ],
            bases=('main.baseretailcategory',),
        ),
        migrations.CreateModel(
            name='DisignService',
            fields=[
                ('baseservicecategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseservicecategory')),
            ],
            bases=('main.baseservicecategory',),
        ),
        migrations.CreateModel(
            name='ITService',
            fields=[
                ('baseservicecategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseservicecategory')),
            ],
            bases=('main.baseservicecategory',),
        ),
        migrations.CreateModel(
            name='MusicService',
            fields=[
                ('baseservicecategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseservicecategory')),
            ],
            bases=('main.baseservicecategory',),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('design', 'Design'), ('it', 'It'), ('music', 'Music')], max_length=100)),
                ('has_office', models.BooleanField()),
                ('office_area', models.FloatField()),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.business')),
            ],
        ),
        migrations.AddField(
            model_name='baseservicecategory',
            name='service_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicetype'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='servicetype',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
        migrations.CreateModel(
            name='RetailType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_category', models.CharField(choices=[('books', 'Books'), ('sport', 'Sport'), ('clothes', 'Clothes')], max_length=100)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CateringType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catering_type', models.CharField(choices=[('bar', 'Catering'), ('coffee house', 'Coffee house'), ('restaurant', 'Restaurant'), ('burger joint', 'Burger joint')], max_length=100)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
        migrations.AddField(
            model_name='baseservicecategory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
        migrations.AddField(
            model_name='baseretailcategory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
        migrations.AddField(
            model_name='basecateringtype',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
    ]