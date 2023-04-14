# Generated by Django 4.2 on 2023-04-11 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=30)),
                ('f_occupation', models.CharField(max_length=20)),
                ('f_phone_no', models.CharField(max_length=10)),
                ('mother_name', models.CharField(max_length=30)),
                ('m_occupation', models.CharField(max_length=20)),
                ('m_phone_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_fname', models.CharField(max_length=30)),
                ('t_lname', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('t_phone_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('mothertounge', models.CharField(max_length=10)),
                ('admission_no', models.CharField(max_length=10)),
                ('st_par', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.parent')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_paid', models.CharField(max_length=10)),
                ('fee_remaining', models.CharField(max_length=10)),
                ('history', models.DateField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]