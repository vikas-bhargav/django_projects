from django.db import models

# Create your models here.


class Projects(models.Model):
    project_name = models.CharField(max_length=200, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.project_name
