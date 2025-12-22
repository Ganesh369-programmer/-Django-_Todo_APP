from django.db import models
from django.contrib.auth.admin import User # this is Django Built in Function (use for - login , signup , authentication , linking data to user)


class TODOO(models.Model):
    srno = models.AutoField(primary_key=True , auto_created=True)
    #(AutoField) - auto increment Integer

    title = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)  #Automatically stores current date & time
    user = models.ForeignKey(User , on_delete=models.CASCADE)   # this line defines all Todo list belogs to on user
    #(on_delete=models.CASCADE) :- this line defines the when user is delete then all todo list will be deleted 

    def __str__(self):
        return self.title














