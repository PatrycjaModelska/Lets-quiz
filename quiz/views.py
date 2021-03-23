from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from .models import Quiz, Result


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'


@login_required
def quiz_view(request, pk):
    if request.method == 'POST':
        quiz = Quiz.objects.get(id=pk)
        score = 0
        result, created = Result.objects.get_or_create(quiz=quiz, user=request.user.profile)

        results =[]

        for question in quiz.get_question():  # dla każdego pytania w formularzu
            user_answer_id = request.POST[str(question.id)]  #sprawdzam id odpowiedzi użytkownika
            user_answer = question.get_answer().get(id=user_answer_id)  # znajduje odpoedź
            correct_answer = question.get_answer().get(is_correct=True)  # sprawdzam jaka jest dobra odpowiedź
            if user_answer == correct_answer:  # porównuję odpowiedź użytkownika z prawidłową odpwiedzią:
                score += 1
            results.append([question.id, user_answer, correct_answer])
        
        result.score = score
        result.save()

        return redirect('quiz_result', pk)

    else:
        quiz = Quiz.objects.get(id=pk)
        return render(request, 'quiz_view.html', {'quiz': quiz})


@login_required
def quiz_result(request, pk):
    result = Result.objects.filter(quiz=pk, user=request.user.profile).first
    return render(request, 'quiz_result.html', {'result': result})

