<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Designer

# views.py의 pk 변수명과 urls.py의 pk변수명은 같아야한다!
# Create your views here.
def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers})
    
def introduce(request):
    return render(request, 'introduce.html')

def detail(request, designer_id):
    detail = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})

=======
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def introduce(request):
    return render(request, 'introduce.html')
>>>>>>> 35d38f25ae405a89056a71bd64ce2e830f3a7c84
