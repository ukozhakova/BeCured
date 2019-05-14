# Generated by Django 2.2.1 on 2019-05-13 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_doctor_patient_diagnosis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[(1, 'ADMIN'), (2, 'DOCTOR'), (3, 'RECEPTIONIST'), (4, 'PATIENT')], default=1, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to='api.Person'),
        ),
        migrations.AddField(
            model_name='patient',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to='api.Person'),
        ),
        migrations.AddField(
            model_name='receptionist',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recep_profile', to='api.Person'),
        ),
    ]