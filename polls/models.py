from django.db import models

# Create your models here.
class UserData(models.Model):
    def __str__(self):
        return self.tele_text
    nom_text = models.CharField(max_length=20)
    prenom_text = models.CharField(max_length=20)
    tele_text = models.CharField(max_length=20)
    email_text = models.EmailField(max_length=50)
    passeport_text = models.CharField(max_length=20)
    startprocess_date = models.DateTimeField('processdata')
    endprocess_date = models.DateTimeField('endprocessdata')
    state_int = models.IntegerField()
    notifytele_text = models.CharField(max_length=20)