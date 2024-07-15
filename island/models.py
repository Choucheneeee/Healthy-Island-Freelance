from django.db import models

# Create your models here.
class Plat (models.Model):
    time_choices = [
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
    ]
    type_choices = [
        ('Dishes', 'Dishes'),
        ('Drinks', 'Drinks'),
        ('Desserts', 'Desserts'),
    ]
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    bio = models.CharField(max_length=100,blank=True,null=True)
    image1 = models.ImageField(upload_to='images/',blank=True, null=True)
    image2 = models.ImageField(upload_to='images/',blank=True, null=True)
    image3 = models.ImageField(upload_to='images/',blank=True, null=True)
    image4 = models.ImageField(upload_to='images/',blank=True, null=True)
    price = models.IntegerField(default=0,blank=True, null=True)
    serve = models.IntegerField(default=0)
    description = models.CharField(max_length=3000,blank=True, null=True)
    Calories= models.IntegerField(default=0)
    ingridients= models.CharField(max_length=380, blank=True, null=True)
    type=models.CharField(max_length=20, choices=type_choices, blank=True, null=True)
    time=models.CharField(max_length=20, choices=time_choices, blank=True, null=True)
    


class Reservation (models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=3000,blank=True, null=True)
    email =models.CharField(max_length=3000,blank=True, null=True)
    time=models.TimeField(max_length=20,blank=True, null=True)
    serve = models.IntegerField(default=0)
    date =models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At', blank=True, null=True)


    