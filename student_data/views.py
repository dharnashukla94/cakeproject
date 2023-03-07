from django.shortcuts import render
from .models import StudentDetails, Course
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def student_info(request):
    course1 = Course(cid='C005', course_name='Perl', duration='30 hours')
    course1.save()
    course = Course.objects.get(cid='C005')
    student1 = StudentDetails(sid='S005', name='Mark', course_id=course)
    student1.save()

    print("data added successfully")

    # # fetch data
    #
    # fetch1 = StudentDetails.objects.get(name='Renee')
    # fetch_name = fetch1.course_id.course_name
    # print("course for user is ", fetch_name)
    #
    # # Delete the user from student table
    # data1 = StudentDetails.objects.filter(name='john').delete()
    # print('data is deleted from table', data1)
    #
    # # delete from course table
    # data2 = Course.objects.filter(cid='C004').delete()
    # print('data is deleted from table', data2)

    message = 'Course and student added successfully!'
    return render(request, 'students.html', {'message': message})


def query_set(request):

    data1 = StudentDetails.objects.all().values('sid')
    data2 = StudentDetails.objects.filter(Q(sid='S001') | Q(course_id='C001')).values()
    #data2 = StudentDetails.objects.filter(sid='S004').values() | StudentDetails.objects.filter(course_id='C004').values()
    data3 = StudentDetails.objects.filter(Q(name='Renee') | Q(name='Mark')).values()

    # where condition use, field lookups

    data4 = StudentDetails.objects.filter(name__istartswith='r').values()

    # JOINS
    data5 = StudentDetails.objects.get(course_id='cid')
    cdata = data5.course_id.course_name

    context = {
        'd1': data1,
        'd2': data2,
        'd3': data3,
        'd4': data4,
        'd5': cdata
    }
    return render(request, 'students.html', context)




