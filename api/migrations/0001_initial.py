# Generated by Django 3.0.6 on 2020-06-23 00:03

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('zip_code', models.TextField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('how_many_jobs', models.TextField(blank=True, null=True)),
                ('stars_value', models.TextField(blank=True, null=True)),
                ('distance_in_miles', models.TextField(blank=True, null=True)),
                ('specializes', models.TextField(blank=True, null=True)),
                ('last_reviews', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('seller', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('first_name', models.CharField(default='null', max_length=40)),
                ('last_name', models.CharField(default='null', max_length=140)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('customer_id', models.TextField(blank=True, max_length=120)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('pay', models.TextField(blank=True, null=True)),
                ('job_price', models.FloatField(blank=True, null=True)),
                ('job_hours', models.IntegerField(blank=True, null=True)),
                ('job_type', models.TextField(blank=True, null=True)),
                ('job_media', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('price_per_hour', models.TextField(blank=True, null=True)),
                ('job_time', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Buyer_job', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_job', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('offer_price', models.FloatField(blank=True, null=True)),
                ('offer_hours', models.IntegerField(blank=True, null=True)),
                ('offer_type', models.TextField(blank=True, null=True)),
                ('offer_media', models.FileField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('price_per_hour', models.IntegerField(blank=True, null=True)),
                ('offer_time', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Buyer_offer', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_offer', to='api.Job')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_offer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Review_buyer', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Job')),
                ('sller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('status', models.TextField(choices=[('created', 'Created'), ('paid', 'Paid'), ('abandoned', 'Abandoned')], default='created', max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('payment_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('succeful', models.BooleanField(default=False)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Buyer_user', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Job')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Offer')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.TextField(max_length=120)),
                ('paid', models.BooleanField(default=False)),
                ('refunded', models.BooleanField(default=False)),
                ('outcome', models.TextField(blank=True, null=True)),
                ('outcome_type', models.TextField(blank=True, max_length=120, null=True)),
                ('seller_message', models.TextField(blank=True, max_length=120, null=True)),
                ('risk_level', models.TextField(blank=True, max_length=120, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.PaymentOrder')),
            ],
        ),
    ]
