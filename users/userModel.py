from django.db import models

# Create your models here.
class Users(models.Model):
    Id = models.BigIntegerField(null=False, auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = "Users"