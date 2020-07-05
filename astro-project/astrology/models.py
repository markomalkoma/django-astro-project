from django.db import models


class Tipo(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Nata(models.Model):
    surname=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    year=models.IntegerField()
    month=models.IntegerField()
    day=models.IntegerField()
    hour=models.IntegerField()
    minutes=models.IntegerField()
    precise=models.IntegerField()

    category=models.ManyToManyField(Tipo)
    
    def __str__(self):
        return self.name+' '+self.surname

    
class Position(models.Model):
    sun=models.FloatField()
    moon=models.FloatField()
    mercury=models.FloatField()
    venus=models.FloatField()
    mars=models.FloatField()
    jupiter=models.FloatField()
    saturn=models.FloatField()
    uranus=models.FloatField()
    neptune=models.FloatField()
    pluto=models.FloatField()
    tnode=models.FloatField()
    mnode=models.FloatField()
    lilit=models.FloatField()
    chiron=models.FloatField()

    natus=models.OneToOneField(Nata, on_delete=models.CASCADE)
    

