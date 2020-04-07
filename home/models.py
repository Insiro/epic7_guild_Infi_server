from django.db import models

# Create your models here.


class DefensePreset(models.Model):
    name = models.CharField(max_length=100)
    Defense = models.IntegerField()
    HP = models.IntegerField()


class debuff(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()


class buff(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()


class tips(models.Model):
    link = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    memo = models.TextField(max_length=500, null=True, blank=True)
    important = models.BooleanField(default=False)
    image = models.ImageField(upload_to="epic/image", null=True, blank=True)
    imageLink = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.writer + " : " + self.name


class user(models.Model):
    UID = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    UPW = models.CharField(max_length=100)
    Signed = models.BooleanField(default=False)
    isManager = models.BooleanField(default=False)

    def __str__(self):
        return self.UID + " : " + self.name


class notic(models.Model):
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, null=True)
    contents = models.TextField(max_length=4000, null=True)
    important = models.BooleanField(default=False)
    linkName = models.CharField(max_length=20, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="epic/image", null=True, blank=True)


class Heros(models.Model):
    SearchKey = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    rarity = models.IntegerField()
    classType = models.CharField(max_length=20)
    element = models.CharField(max_length=10)


class BotSkills(models.Model):
    Skill = models.CharField(max_length=30)
    target = models.CharField(max_length=10, null=True, blank=True)
    deiscribe = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.Skill
