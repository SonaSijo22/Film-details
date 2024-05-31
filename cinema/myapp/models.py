from django.db import models

# Create your models here.
  #    1.MOVIE
  # -------------
class Movie(models.Model):
  title=models.CharField(max_length=200,unique=True)
  director=models.CharField(max_length=200)
  year=models.CharField(max_length=200)
  geners=models.CharField( max_length=200)
  poster=models.ImageField(upload_to="images",default="images/default.jpg",blank=True)
  actors=models.CharField( max_length=200)
  run_time=models.PositiveIntegerField()
  description=models.CharField( max_length=5000,null=True)
  writers=models.CharField( max_length=200)
  languages=models.CharField( max_length=200)

  def __str__(self):
      return self.title



      



    

    
  