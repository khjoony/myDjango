"""
My Model
"""
import datetime
from django.db import models
from django.utils import timezone

class Member(models.Model):
    """
    test
    """
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    membership_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20)
    chi_name = models.CharField(max_length=20, null=True)
    en_name = models.CharField(max_length=20, null=True)

    def  to_dict(self):
        """
            test
        """
        return{
            'id' : self.id,
            'membership_id' : self.membership_id,
            'name': self.name,
            'chi_name' : self.chi_name,
            'en_name' : self.en_name,
        }
    def __str__(self):
        return self.name

class Question(models.Model):
    """
        test
    """
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    ## Expression of Object
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        """
            test
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """
        test
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #id = models.AutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    choice_prod = models.CharField(max_length=200, default=None, blank=True, null=True)
    votes = models.IntegerField(default=0)


    def to_dict(self):
        """
            test
        """
        return {
            'ID': self.id,
            'choice_text':self.choice_text,
            'choice_prod':self.choice_prod,
            'question': {
                'ID':self.question.id,
                'question_text':self.question.question_text,
                'pub_date':self.question.pub_date,
            }
        }

    def __str__(self):
        return {self.choice_prod, self.choice_text}


   # ##  사전 타입 출력하기
   # from assembly.models import Question, Choice
   # from django.utils import timezone
   # from pprint import pprint

   # Question.objects.all().delete()
   # questions = Question.objects.bulk_create(
   #     [
   #         Question(
   #             id = i,
   #             question_text = 'question-{}'.format(i),
   #             pub_date = timezone.now(),
   #         )
   #         for i in range(1, 10)
   #     ]
   # )

   # Choice.objects.all().delete()
   # Choice.objects.bulk_create(
   #     [
   #         Choice(
   #             id = i,
   #             choice_text = 'choice-{}'.format(i),
   #             choice_prod = 'TV-{}'.format(i),
   #             question = questions[i],
   #         )
   #         for i in range(1, 10)
   #     ]
   # )
   # pprint([b.to_dict() for b in Choice.objects.all()])
