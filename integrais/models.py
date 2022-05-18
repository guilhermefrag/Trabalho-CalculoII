from django.db import models
from sympycharfield.fields import SympyCharField

class Integral(models.Model):
    id = models.AutoField(primary_key=True)
    f_x = SympyCharField(blank=False, null=False, max_length=20)
    g_x = SympyCharField(blank=False, null=False, max_length=20)
    a = models.CharField(blank=False, null=False, max_length=20)
    b = models.CharField(blank=False, null=False, max_length=20)
    area = models.FloatField()
    valor = models.FloatField()
    class Meta:
        managed = False
        db_table = 'integral'