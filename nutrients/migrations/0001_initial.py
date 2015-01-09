# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('calcium_mg', models.DecimalField(decimal_places=2, max_digits=5, default=0)),
                ('potassium_mg', models.DecimalField(decimal_places=2, max_digits=5, default=0)),
                ('hdl', models.DecimalField(decimal_places=2, max_digits=5, default=0)),
                ('ldl', models.DecimalField(decimal_places=2, max_digits=5, default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
