from django.shortcuts import render

from intro.models import AccessLog

# Create your views here.
def intro(request):
    access_log = AccessLog()
    access_log.location = "intro.html"
    access_log.save()
    
    tt = AccessLog.objects.get(id=1)
    print(tt.created_at)
    
    return render(request,'intro.html')
