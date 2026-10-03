from django.db import models

class News(models.Model): 
    title=models.CharField(max_length=150) 
    content=models.TextField(blank=True) 
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True) 
    photo=models.ImageField(upload_to='photos/%Y/%m/%d') 
    is_published=models.BooleanField(default=True)
    #def __str__(self): 
    #    return self.title

class Products(models.Model):
    name=models.CharField(max_length=150)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField(null=True, default=1)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    in_stock=models.BooleanField(default=True)
    # Метод, чтобы объекты при работе с ORM
    # отображались со своими именами
    def __str__(self): 
        return self.name