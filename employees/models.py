from django.db import models

class Employee(models.Model):

    emp_id = models.CharField(max_length=20, unique=True)

    emp_name = models.CharField(max_length=100)

    email = models.EmailField()

    experience = models.IntegerField()

    primary_skill = models.CharField(max_length=100)

    secondary_skill = models.CharField(max_length=100)

    cm_name = models.CharField(max_length=100)

    profile_status = models.CharField(max_length=100)

    customer = models.CharField(max_length=100)

    date_shared = models.DateField()

    project_owner = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name