from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from .models import Quiz, Result, UserAnswer, Question


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'


@login_required
def quiz_view(request, pk):
    if request.method == 'POST':
        quiz = Quiz.objects.get(id=pk)
        score = 0
        result, created = Result.objects.get_or_create(quiz=quiz, user=request.user.profile)


        for question in quiz.get_question():
            user_answer_id = request.POST[str(question.id)]
            user_answer = question.get_answer().get(id=user_answer_id)
            correct_answer = question.get_answer().get(is_correct=True)
            if user_answer == correct_answer:
                score += 1
            useranswer, created = UserAnswer.objects.get_or_create(user=request.user.profile, question=question)
            useranswer.my_answer = user_answer
            useranswer.correct_answer = correct_answer
            useranswer.save()

        
        result.score = score
        result.save()
        user = request.user.profile
        return redirect('quiz_result', pk, user)

    else:
        quiz = Quiz.objects.get(id=pk)
        return render(request, 'quiz_view.html', {'quiz': quiz})


@login_required
def quiz_result(request, pk, user):
    result = Result.objects.filter(quiz=pk, user=request.user.profile).first
    return render(request, 'quiz_result.html', {'result': result})

def quiz_result_details(request, pk, user):
    quiz = Quiz.objects.get(pk=pk)
    questions = Question.objects.filter(quiz=pk)
    useranswer = UserAnswer.objects.filter(user = request.user.profile , question__in=questions)
    return render(request, 'quiz_result_details.html', {'quiz': quiz, 'questions': questions, 'useranswers': useranswer})

