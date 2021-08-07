from django.db import models

class AnimalModel(models.Model):
    class Meta:
        db_table = "show_animal"
    happenDt = models.DateTimeField(default='')
    orgNm = models.CharField(max_length=500)
    sexCd = models.CharField(max_length=500)
    processState = models.CharField(max_length=500)
    neuterYn = models.CharField(max_length=500)
    specialMark = models.CharField(max_length=500)
    careNm = models.CharField(max_length=500)
    happenPlace	 = models.CharField(max_length=500)
    kindCd = models.CharField(max_length=500)
    colorCd = models.CharField(max_length=500)
    age = models.CharField(max_length=500)
    weight = models.CharField(max_length=500)
    noticeEdt = models.DateTimeField(default='')
    noticeSdt = models.DateTimeField(default='')
    popfile = models.CharField(max_length=500)


