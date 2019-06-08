from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from student.forms import StudentForm
from student.models import Student


def index(request):
    students = Student.object.all()
    if request.method == 'POST':
        form = StudentForm
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reversed('index'))
    else:
        form = StudentForm

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)