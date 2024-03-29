from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@csrf_exempt
def submit_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)
        return HttpResponse("I'll get back to you asap!")
    else:
        return render(request, 'contact.html')

def download_resume(request):
    filepath = '/home/foxhj/workspace/develop/personal_site/static/resume.pdf'
    response = FileResponse(open(filepath, 'rb'), as_attachment=True, filename='Fox_Johnston_Resume.pdf')
    return response