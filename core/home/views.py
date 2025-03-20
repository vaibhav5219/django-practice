from django.shortcuts import render
from home.models import Students
from django.db.models import Q

# Create your views here.


def search_page(request):
    students = Students.objects.all()
    search_param = request.GET.get('search')
    age_param = request.GET.get('age')

    if search_param:
        # students = students.filter(name__icontains = search_param)
        # students = students.filter(college__College_name__icontains = search_param)
        # students = students.filter(email__startswith = search_param)
        # students = students.filter(email__endswith = search_param)
        students = students.filter(
            Q(email__icontains = search_param) |
            Q(name__icontains = search_param)
        )

    if age_param:
        print(age_param, type(age_param))
        if age_param == '1':
            students = students.filter(age__gte = 18, age__lte = 20).order_by('age')
        if age_param == '2':
            students = students.filter(age__gte = 20, age__lte = 22).order_by('age')
        if age_param == '3':
            students = students.filter(age__gte = 22, age__lte = 24)
    
    context = {
        'students' : students,
        'search' : search_param,
    }
    
    return render(request, 'search.html', context)