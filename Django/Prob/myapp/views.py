from django.shortcuts import render
from django.views import View
from .models import New, Rubric


class NewPage(View):
    def get(self, request):
        news = New.objects.all()
        rubrics = Rubric.objects.all()
        # news = {}
        # for r in rubrics:
        #     news[r.name] = New.objects.filter(rubric=r)[:2]
        context = {'news': news, 'rubrics': rubrics}
        return render(request, 'mane_page.html', context)


class RubricPage(View):
    def get(self, request, rubric_id):
        news = New.objects.filter(rubric=rubric_id)
        rubrics = Rubric.objects.all()
        need_rubric = Rubric.objects.get(pk=rubric_id)
        context = {'news': news, 'rubrics': rubrics, 'need_rubric': need_rubric}
        return render(request, 'rubric_page.html', context)


