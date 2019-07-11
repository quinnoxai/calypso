from django.db import models
from django.contrib.auth.models import User
from mongoengine import *
from mongoengine import Document
#     comments = ListField()
from mongoengine import connect

connect('helpdesk')


class IntentFeedback(Document):
    name = StringField()
    user_id =StringField()
    sentence = StringField()
    main_intent=StringField()
    response_status=BooleanField()
    dict_variable=DictField()
    response=StringField()
    timestamp = DateTimeField()



# meta = {'db_alias': 'user_activity'}
class EmployeeFeedback(Document):
    name= StringField()
    user_id = IntField()
    user_feedback = StringField()
    timestamp=DateTimeField()

class LetterTable(Document):
    name= StringField()
    response = StringField()
    user_id = IntField()
    sentence=StringField()
    model_intent=StringField()
    main_intent=StringField()
    dict_info=DictField()
    timestamp=DateTimeField()

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
    return self.user.username
