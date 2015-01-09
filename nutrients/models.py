from django.db import models

# Create your models here.

from django.db import models


class Foods(models.Model):
    food_name = models.CharField(max_length=200)
    calcium_mg = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    potassium_mg = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    hdl = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    ldl = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    pub_date = models.DateTimeField('date published')


#class Choice(models.Model):
#    question = models.ForeignKey(Question)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

