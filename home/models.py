from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.IntegerField()
    product_name=models.TextField()
    price=models.FloatField()
    description=models.TextField()
    category=models.TextField()
    picture=models.ImageField(default='white.jpg')

    def __str__(self):
        return str(self.product_id)+" "+self.product_name+" "+str(self.price)

    class Meta:
        db_table='products'