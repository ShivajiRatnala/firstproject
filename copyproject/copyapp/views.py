from django.shortcuts import render

# Create your views here.
from copyapp.models import Student
def student_view(request):
    student_list = Student.objects.all()
    return render(request,'testapp/std.html',{'student_list':student_list})