# Generated by Django 2.2.7 on 2020-02-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(db_index=True, max_length=200)),
                ('airline_code', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ('airline_code',),
            },
        ),
        migrations.AlterField(
            model_name='program',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tkt_programs', to='tours.Ticket'),
        ),
    ]
