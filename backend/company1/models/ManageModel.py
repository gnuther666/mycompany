from django.db import models

class TaskUserTypeModel(models.Model):
    id = models.AutoField(primary_key=True)
    UserEn = models.CharField(max_length=30)
    UserCn = models.CharField(max_length=100)

    def __str__(self):
        return "%.06s:[%030s]%050s" % (str(self.id), self.UserEn, self.UserCn)

    class Meta:
        ordering = ['id']
        db_table = 'TaskUserType'

class MenuConfigModel(models.Model):
    id = models.AutoField(primary_key=True)
    ParentId = models.IntegerField(blank=False, default=0)
    MenuEn = models.CharField(max_length=30)
    MenuCn = models.CharField(max_length=70)
    IsNeedSuper = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        db_table = 'MenuConfig'