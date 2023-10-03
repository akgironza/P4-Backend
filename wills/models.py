from django.db import models

# Create your models here.

class Will(models.Model):
    user_name = models.CharField(max_length=100)
    user_address = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    user_tax_id = models.CharField(max_length=100)
    created_when = models.DateTimeField()

class Asset(models.Model):
    will = models.ForeignKey(Will, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)

class Inheritor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    active = models.BooleanField()

class InheritorGroup(models.Model):
    inheritor = models.ForeignKey(Inheritor, on_delete=models.DO_NOTHING)
    grouping_key = models.IntegerField()
    priority = models.IntegerField()

class Distribution(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    inheritor_group = models.ForeignKey(InheritorGroup, on_delete=models.CASCADE)
    percentage = models.FloatField()
    distributed = models.BooleanField()

# ALTER TABLE "asset" ADD FOREIGN KEY ("will_id") REFERENCES "will" ("id");

# ALTER TABLE "inheritor_group" ADD FOREIGN KEY ("inheritor_id") REFERENCES "inheritor" ("id");

# ALTER TABLE "distribution" ADD FOREIGN KEY ("asset_id") REFERENCES "asset" ("id");

# ALTER TABLE "distribution" ADD FOREIGN KEY ("inheritor_group_id") REFERENCES "inheritor_group" ("id");
