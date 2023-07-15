from django.db import models

class Banner(models.Model):
    photo = models.FileField()
    text = models.TextField()


class Banner_video(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
    is_file = models.BooleanField()
    video_file = models.FileField(null=True, blank=True)
    video = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural = "Banner_video"
        ordering = ["name", ]


class Players(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    position = models.CharField(max_length=255)
    games = models.IntegerField()
    time_game = models.IntegerField()
    start = models.IntegerField()
    sub_off = models.IntegerField()


class Shop(models.Model):
    team_name = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    img = models.ImageField()


class Stadium_info(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    volume = models.IntegerField()
    places = models.IntegerField()
    location = models.TextField()
    phone = models.IntegerField()


class Logo(models.Model):
    img = models.ImageField()


class Information(models.Model):
    logo = models.ImageField()
    text = models.TextField()
    inst = models.CharField(max_length=255)
    tg = models.CharField(max_length=255)
    fb = models.CharField(max_length=255)
    yut = models.CharField(max_length=255)
    tw = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()


class Administrator(models.Model):
    img = models.FileField()
    name = models.CharField(max_length=255)
    text = models.TextField()


class Coaches(models.Model):
    img = models.FileField()
    name = models.CharField(max_length=255)
    text = models.TextField()


class History(models.Model):
    achievements = models.TextField()
    achiv_img = models.ImageField()
    achiv_text = models.TextField()
    ceremonies = models.TextField()
    img = models.ImageField()


class Goal(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()


class Recommendations(models.Model):
    img = models.ImageField()
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()


class Training(models.Model):
    img = models.ImageField()


class Tims(models.Model):
    name = models.CharField(max_length=50)
    games = models.IntegerField()
    win = models.IntegerField()
    draw = models.IntegerField()
    lose = models.IntegerField()
    t_f = models.IntegerField()
    o = models.IntegerField()
    img = models.ImageField(upload_to="Jadval/")
    
    def __str__(self):
        return self.name
    
