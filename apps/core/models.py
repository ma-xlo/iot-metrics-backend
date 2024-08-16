# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Metrics(models.Model):
    deviceid = models.CharField(db_column='deviceId', max_length=50)  # Field name made lowercase.
    cpu_temperature = models.FloatField(blank=True, null=True)
    available_memory = models.FloatField(blank=True, null=True)
    uptime = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField()
    ram_usage_value = models.FloatField(blank=True, null=True)
    ram_usage_percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metrics'
