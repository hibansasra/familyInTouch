# Generated by Django 3.2.16 on 2023-01-07 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('customer_id', models.CharField(max_length=9, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('password', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100, null=True)),
                ('feedback', models.CharField(max_length=1200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('shift_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('shift_name', models.CharField(choices=[('shift1', 'shift1'), ('shift2', 'shift2'), ('shift3', 'shift3')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('day_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('day_name', models.CharField(choices=[('sunday', 'sunday'), ('moneday', 'moneday'), ('tuesday', 'tuesday'), ('wensday', 'wensday'), ('thersday', 'thersday')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('worker_id', models.CharField(max_length=9, null=True)),
                ('bank_acccount', models.CharField(max_length=16, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDayShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=200, null=True)),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ourproject.weekday')),
                ('shift', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ourproject.shift')),
            ],
        ),
        migrations.AddField(
            model_name='weekday',
            name='shifts',
            field=models.ManyToManyField(through='ourproject.WeekDayShift', to='ourproject.Shift'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('bar_code', models.CharField(max_length=10, null=True)),
                ('price', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Pen-Markers', 'Pen-Markers'), ('Paint', 'Paint'), ('Brushes', 'Brushes'), ('Art paper&board', 'Art paper&board'), ('Canvas', 'Canvas'), ('Drawing media', 'Drawing media')], max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('tags', models.ManyToManyField(to='ourproject.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('name_of_product', models.CharField(max_length=200, null=True)),
                ('customer_name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ourproject.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ourproject.product')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ourproject.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ourproject.product')),
            ],
        ),
    ]