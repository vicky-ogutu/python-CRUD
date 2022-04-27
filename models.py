from django.db import models

class main_clientsModel(models.Model):
    client_id= models.IntegerField(auto_created=True, primary_key=True)
    client_name= models.CharField(max_length=100)
    client_county= models.CharField(max_length=100)
    client_age = models.IntegerField()

    class Meta:
        db_table="main_clients"

        