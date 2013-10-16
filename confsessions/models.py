from django.db import models
from django.contrib.auth.models import User

class SessionTime(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class SessionType(models.Model):
    session_time = models.ForeignKey(SessionTime)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Session(models.Model):
    sessiontype = models.ForeignKey(SessionType)
    name = models.CharField(max_length=200)
    presenter = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    teaser = models.CharField(max_length=2000)
    description = models.CharField(max_length=5000)
    participants = models.ManyToManyField(User)
    def add_participant(self,User):
        for sess_type in self.sessiontype.session_time.sessiontype_set.all():
            for sess in sess_type.session_set.all():
                sess.participants.remove(User)
        self.participants.add(User)

    def has_spaces(self):
        spaces = self.capacity - self.participants.count()
        if spaces <=0:
            return False
        else: 
            return True
    
    def registered_delegates(self):
        return str(self.participants.count())

    def percent_spaces(self):
        percent = 1-float(self.participants.count())/self.capacity
        return str(percent*100) + "%"


    def capacity_color(self):
        percent = 1-float(self.participants.count())/self.capacity
        if percent <= 0:
            return "full" 
        if percent <= .15:
            return "redbar"
        if percent <= .5:
            return "yellowbar"
        return "greenbar" 

    def __unicode__(self):
        return self.name

'''class MySessions(models.Model):
    session = models.ForeignKey(Session)
    participant = models.ManyToManyField(User)
    def __unicode__(self):
        return self.session
        '''
