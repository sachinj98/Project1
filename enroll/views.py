from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.

# This Function used to Addnew Student and show the info of that student
def add_show(request):
    if request.method == "POST":                   # method to save the data in our database
        obj = StudentRegistration(request.POST)
        if obj.is_valid():                       # we can save the our data directly using .save() method
            # name = obj.changed_data['name']
            # email = obj.changed_data['email']
            # password = obj.changed_data['password']
            # phone = obj.changed_data['phone']
            # reg = Student(name = name, email = email, password = password, phone = phone)
            obj.save()                           # another way to save the data is cleaned_data method
            obj = StudentRegistration()    
    else:
        obj = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': obj, 'stu': stud})




def update_data(request, id):
    if request.method == 'POST':
        ud = Student.objects.get(pk=id)
        obj1 = StudentRegistration(request.POST, instance=ud)
        if obj1.is_valid():
            obj1.save()
    else:
        ud = Student.objects.get(pk=id)
        obj1 = StudentRegistration(instance=ud)      
    return render(request, 'enroll/updatestudent.html', {'form': obj1})
        




def delete_info(request, id):
    if request.method == "POST":
        dl = Student.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')
    



