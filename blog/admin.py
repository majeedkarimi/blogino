from django.contrib import admin
from .models import User,Post,Comment,Label,Post_Label,Category,SubCategory,Like_Post,Like_Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Label)
admin.site.register(Post_Label)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Like_Post)
admin.site.register(Like_Comment)
