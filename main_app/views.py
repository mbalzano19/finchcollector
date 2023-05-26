from django.shortcuts import render

finches = [
  {'name': 'Curtis', 'purple finch': 'tabby', 'description': 'furry little guy', 'age': 3},
  {'name': 'Henry', 'zebra finch': 'calico', 'description': 'wise elder', 'age': 29},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })