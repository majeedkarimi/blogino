from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name=models.CharField('دسته بندی',max_length=100)


class SubCategory(models.Model):
    sub_name=models.CharField('زیر دسته',max_length=100)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

    
class User(models.Model):
    firstname=models.CharField('نام',max_length=100)
    lastname=models.CharField('نام خانوادگی',max_length=100)
    email = models.EmailField('ایمیل',max_length=70,blank=True, null= True, unique= True)    
    phone=models.IntegerField('شماره تلفن',)
    image=models.ImageField('عکس',)
      

class Post(models.Model):
    title=models.CharField('عنوان',max_length=100)
    text=models.CharField('متن',max_length=1000)
    image = models.ImageField('تصویر')
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)  

    
class Comment(models.Model):
    text=models.CharField('متن',max_length=1000)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)   
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)  


class Label(models.Model):
    text=models.CharField('متن',max_length=100)


class Post_Label(models.Model):
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    label_id=models.ForeignKey(Label,on_delete=models.CASCADE)   

    
class Like_Comment(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_id=models.ForeignKey(Comment,on_delete=models.CASCADE)
    like=models.BooleanField()

    
class Like_Post(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    like=models.BooleanField()