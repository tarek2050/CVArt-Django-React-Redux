# Generated by Django 3.2.5 on 2021-08-17 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_rename_title_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('firstName', models.CharField(blank=True, max_length=250, null=True)),
                ('lastName', models.CharField(blank=True, max_length=250, null=True)),
                ('professionalTitle', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('birthday', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('facebook', models.URLField(blank=True, max_length=250, null=True)),
                ('instagram', models.URLField(blank=True, max_length=250, null=True)),
                ('github', models.URLField(blank=True, max_length=250, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=250, null=True)),
                ('gmail', models.URLField(blank=True, max_length=250, null=True)),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(blank=True, max_length=250, null=True)),
                ('skillValue', models.CharField(blank=True, max_length=200, null=True)),
                ('skill_connected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languageName', models.CharField(blank=True, max_length=250, null=True)),
                ('languageValue', models.CharField(blank=True, max_length=200, null=True)),
                ('language_connected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('dateFrom', models.CharField(blank=True, max_length=100, null=True)),
                ('dateTo', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('experience_connected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('dateFrom', models.CharField(blank=True, max_length=100, null=True)),
                ('dateTo', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('education_connected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
    ]
