from django.db import models
from  django.contrib.auth.models import User

class SkillCategory(models.Model):

    name = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    # host =
    # topic =
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, default=None)

    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name