from datetime import datetime
from django.shortcuts import render

def home(request):
    now = datetime.now()
    hour = now.hour
    
    if 6 <= hour < 12:
        greeting = 'Good Morning!'
    elif 18 <= hour < 24 or 0 <= hour < 6:
        greeting = 'Good Evening!'
    else:
        greeting = f"It's {datetime.strftime(now, '%I %p')}!"
        
    context = {'greeting': greeting}
    return render(request, 'home.html', context)