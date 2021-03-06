# Generated by Django 2.2.1 on 2019-05-13 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190513_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100, null=True)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=10)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
                ('phone_number', models.CharField(default=0, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='person',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='person',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='username',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='name',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='person',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='username',
        ),
        migrations.AddField(
            model_name='patient',
            name='homedoctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='doctor',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Profile'),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Profile'),
        ),
        migrations.AddField(
            model_name='receptionist',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Profile'),
        ),
    ]
