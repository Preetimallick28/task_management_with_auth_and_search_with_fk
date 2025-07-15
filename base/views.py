from django.shortcuts import render

#yellow_underline - currently vscode , this project is using system python software, from system python software we are using for download venv module
# this underline means changing python interpreter - this point should kept in mind
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')