from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.



# ! blabla.com/category/some-category ! #
class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(null = False , blank = True , unique = True , db_index = True , editable = False)
    
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super().save(*args , **kwargs)
    
    
    def __str__(self):
        return f"{self.name}"




# ! null comes false in default , if you want something to be null => null = True ! #
class Language(models.Model):
    title = models.CharField(max_length = 100 , null = True)
    image = models.ImageField(upload_to = "languages")
    description = RichTextField(null = False , default = "")
    is_active = models.BooleanField(default = False)
    is_home = models.BooleanField(default = False)
    is_front = models.BooleanField(default = True)
    is_back = models.BooleanField(default = True)
    is_full = models.BooleanField(default = True)
    slug = models.SlugField(null = False , blank = True , unique = True , db_index = True , editable = False)
    # ! if we want to associate a subset of a class with another class, we use foreign key code ! #
    # category = models.ForeignKey(Category , on_delete = models.CASCADE)
    category = models.ManyToManyField(Category , blank= True)
    
    
    
    #  ! To display the title of classes on admin panel ! #
    def __str__(self):
        return f"{self.title}"
    
    # ! to create slug , we import slugify up there and use this method ! #
    def save(self , *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    




class Frameworks(models.Model):
    title = models.CharField(max_length = 100 , null = True)
    image = models.ImageField(upload_to = "languages")
    description = RichTextField(null = False , default = "")
    is_active = models.BooleanField(default = False)
    is_home = models.BooleanField(default = False)
    is_front = models.BooleanField(default = True)
    is_back = models.BooleanField(default = True)
    is_full = models.BooleanField(default = True)
    slug = models.SlugField(null = False , blank = True , unique = True , db_index = True , editable = False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super().save(*args , **kwargs)
    
    
class Libraries(models.Model):
    title = models.CharField(max_length = 100 , null = True)
    image = models.ImageField(upload_to = "languages")
    description = RichTextField(null = False , default = "")
    is_active = models.BooleanField(default = False)
    is_home = models.BooleanField(default = False)
    is_front = models.BooleanField(default = True)
    is_back = models.BooleanField(default = True)
    is_full = models.BooleanField(default = True)
    category = models.ManyToManyField(Category)

    slug = models.SlugField(null = False , blank = True , unique = True , db_index = True , editable = False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super().save(*args , **kwargs)
    