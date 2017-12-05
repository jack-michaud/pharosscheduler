from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "index.html", {})

def submission(request):
    import pdb; pdb.set_trace()
    params = request.POST

    
