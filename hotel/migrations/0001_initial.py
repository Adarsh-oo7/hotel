# Generated by Django 5.0.1 on 2024-07-14 10:56

import django.db.models.deletion
import django_ckeditor_5.fields
import shortuuid.django_fields
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Processing', 'Processing'), ('cancelled', 'cancelled'), ('Initiated', 'Initiated'), ('refunding', 'refunding'), ('refunded', 'refunded'), ('unpaid', 'unpaid'), ('expired', 'expired')], max_length=100)),
                ('full_name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('before_discount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('saved', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total_days', models.PositiveIntegerField()),
                ('num_adults', models.PositiveIntegerField()),
                ('num_children', models.PositiveIntegerField()),
                ('check_in', models.BooleanField(default=False)),
                ('check_out', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('checked_in_tracker', models.BooleanField(default=False)),
                ('checked_out_tracker', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('strip_payment_intent', models.CharField(blank=True, max_length=1000, null=True)),
                ('success_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('booking_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=10, max_length=20, prefix='', unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_out', models.DateTimeField()),
                ('guess_in', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('image', models.FileField(upload_to='hotel_galley')),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=110)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Disabled', 'Disabled'), ('Rejected', 'Rejected'), ('In Review', 'In Review'), ('Live', 'Live')], default='Live', max_length=20)),
                ('views', models.IntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
                ('hid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=10, max_length=20, prefix='', unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotel'),
        ),
        migrations.CreateModel(
            name='HotelFaqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel FAQs',
            },
        ),
        migrations.CreateModel(
            name='HotelFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_type', models.CharField(blank=True, choices=[('Bootstrap Icons', 'Bootstrap Icons'), ('Fontawesome Icone', 'Fontawesome Icons'), ('Box Icons', 'Box Icons'), ('Remi Icone', 'Remi Icone'), ('Flat Icons', 'Flat Icons')], max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel Features',
            },
        ),
        migrations.CreateModel(
            name='HotelGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='hotel_gallery')),
                ('hgid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=10, max_length=20, prefix='', unique=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Hotel Gallery',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=1000)),
                ('is_available', models.BooleanField(default=True)),
                ('rid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_types', to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ManyToManyField(to='hotel.room'),
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=122)),
                ('number_of_beds', models.PositiveIntegerField(default=0)),
                ('room_capacity', models.PositiveBigIntegerField(default=0)),
                ('rtid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=10, max_length=20, prefix='', unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
            options={
                'verbose_name_plural': 'Room type',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.roomtype'),
        ),
        migrations.CreateModel(
            name='StaffOnDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.booking')),
            ],
        ),
    ]
