from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='base_created_by')
    udpated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='base_updated_by')
    is_deleted = models.BooleanField()

    class Meta:
        abstract = True

    JANUARY = "JAN"
    FEBRUARY = "FEB"
    MARCH = "MAR"
    APRIL = "APR"
    MAY = "MAY"
    JUNE = "JUN"
    JULY = "JUL"
    SEPTEMBER = "SEP"
    OCTOBER = 'OCT'
    NOVEMBER = "NOV"
    DECEMBER = "DEC"

    months_choices = (
        (JANUARY, "JAN"),
        (FEBRUARY, "FEB"),
        (MARCH, "MAR"),
        (APRIL, "APR"),
        (MAY, "MAY"),
        (JUNE, "JUN"),
        (JULY, "JUL"),
        (SEPTEMBER, "SEP"),
        (OCTOBER, 'OCT'),
        (NOVEMBER, "NOV"),
        (DECEMBER, "DEC")
    )


class Units(models.Model):
    name = models.CharField(max_length=40)
    unit_symbol = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class DataType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    url = models.URLField()
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null= True, blank=True)

    def __str__(self):
        return self.url

class Season(models.Model):
    name = models.CharField(max_length=5)
    months = ArrayField(models.CharField(max_length=4))


class TmaxMonthWise(models.Model):

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=4, choices=Base.months_choices)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    value = models.FloatField()


class TminMonthWise(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=4, choices=Base.months_choices)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    value = models.FloatField()


class TmeanMonthWise(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=4, choices=Base.months_choices)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    value = models.FloatField()


class SunshineMonthWise(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=4, choices=Base.months_choices)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    value = models.FloatField()

class RainfallMonthWise(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=4, choices=Base.months_choices)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    value = models.FloatField()



