from django.shortcuts import render, redirect
from .forms import Form1
from .models import Student


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Form1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = Form1()
    return render(request, 'index.html', {'form': form})


def show(request):
    student = Student.objects.all()
    return render(request, 'show.html', {'student': student})


def delete(request, id):
    delete_st = Student.objects.get(pk=id)
    delete_st.delete()
    return redirect('show')


def update(request, id):
    if request.method == 'POST':
        update_st = Student.objects.get(pk=id)
        form = Form1(request.POST, instance=update_st)
        if form.is_valid():
            form.save()
            return redirect('show')
    form = Form1()
    return render(request, 'update.html', {'form': form})
