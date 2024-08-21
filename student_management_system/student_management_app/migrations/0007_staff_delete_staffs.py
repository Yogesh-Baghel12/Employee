# Generated by Django 4.2.2 on 2024-08-19 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_staffs_delete_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=15)),
                ('DOB', models.DateField()),
                ('DOJ', models.DateField()),
                ('tenth_percentage', models.DecimalField(decimal_places=1, help_text='Percentage obtained in 10th grade', max_digits=3)),
                ('twelfth_percentage', models.DecimalField(decimal_places=1, help_text='Percentage obtained in 12th grade', max_digits=3)),
                ('graduation_percentage', models.DecimalField(decimal_places=1, help_text='Percentage obtained in 12th grade', max_digits=3)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=150)),
                ('father_name', models.CharField(max_length=150)),
                ('mother_name', models.CharField(max_length=150)),
                ('father_occupation', models.CharField(max_length=150)),
                ('mother_occupation', models.CharField(max_length=150)),
                ('father_mobile', models.IntegerField()),
                ('role', models.CharField(max_length=150)),
                ('official_mail', models.EmailField(max_length=254)),
                ('personal_email', models.EmailField(max_length=254)),
                ('pancard', models.CharField(max_length=12)),
                ('adharcard', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('departement_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.departement')),
            ],
        ),
        migrations.DeleteModel(
            name='Staffs',
        ),
    ]
