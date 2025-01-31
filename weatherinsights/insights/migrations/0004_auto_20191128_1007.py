# Generated by Django 2.2.7 on 2019-11-28 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0003_auto_20191128_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmaxmonthwise',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tmaxmonthwise',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tmaxmonthwise',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='tmaxmonthwise',
            name='udpated_at',
        ),
        migrations.RemoveField(
            model_name='tmaxmonthwise',
            name='udpated_by',
        ),
        migrations.AddField(
            model_name='datasource',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='insights.Units'),
        ),
        migrations.CreateModel(
            name='RainfallMonthWise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.CharField(choices=[('JAN', 'JAN'), ('FEB', 'FEB'), ('MAR', 'MAR'), ('APR', 'APR'), ('MAY', 'MAY'), ('JUN', 'JUN'), ('JUL', 'JUL'), ('SEP', 'SEP'), ('OCT', 'OCT'), ('NOV', 'NOV'), ('DEC', 'DEC')], max_length=4)),
                ('value', models.FloatField()),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insights.Region')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insights.Units')),
            ],
        ),
    ]
