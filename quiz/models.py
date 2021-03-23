from django.db import models
from account.models import Profile


class Quiz(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_question(self):
        return self.questions.all()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text
    
    def get_answer(self):
        return self.answers.all() # second option self.answer_set.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user} rozwiązała quiz {self.quiz} z wynikiem {self.score}"
