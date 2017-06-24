from django.db import models


class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    parent_category_id = models.IntegerField(null=True)
    channel = models.ForeignKey(Channel)

    def __str__(self):
        return self.name
