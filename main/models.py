from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
    

# # to create new group, add PERMISSIONS to that group, and add any USER to that group "programmatically" write this below commands..... but doing this using django-admin-panel is more easy
# 
# >>> from django.contrib.auth.models import Group, Permission, User
# >>> from django.contrib.contenttypes.models import ContentType

# >>> mod, created = Group.objects.get_or_create(name="mod")
# >>> from main.models import Post
# 
# >>> ct = ContentType.objects.get_for_model(model=Post)
# >>> perms = Permission.objects.filter(content_type=ct)
# >>> mod.permissions.add(*perms)
# 
# to add specific user to mod group
# >>> user = User.objects.filter(username="chaitanya")
# >>> mod.user_set.add(user.first())
# 
#
