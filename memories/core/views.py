from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import MemoryPlaceForm
from .models import MemoryPlace


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    memory_set = MemoryPlace.objects.filter(user=request.user).all()
    return render(request, 'home.html', {'memory_set': memory_set})


@login_required
def create_memory(request):
    m_form = MemoryPlaceForm()
    return render(request, 'create-memory.html', {'m_form': m_form})


@login_required
def save_memory(request):
    if request.method == "POST":
        m = MemoryPlaceForm(request.POST)
        print(m.errors)
        if m.is_valid():
            m.instance.user = request.user
            m.save()
            return redirect('/')
        else:
            return HttpResponse('Failed due to data')
    else:
        return HttpResponse('Method is not supported')
