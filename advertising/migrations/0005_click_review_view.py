# Generated by Django 3.1.3 on 2020-11-11 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0004_auto_20201111_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='advertising.ad')),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='advertising.review')),
            ],
            bases=('advertising.review',),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='advertising.review')),
            ],
            bases=('advertising.review',),
        ),
    ]
