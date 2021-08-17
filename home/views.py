from django.shortcuts import render
from .session_manager import options


def home(request):
	j = request.session
	
	session=options(request)
	
	
	
	
		
	return render(request, 'index.html', {'cookies': session['cookies'], 'wantToPlay': session['wantToPlay'], 'userIsLogin': session['userIsLogin'], 'gameMode' : session['gameMode'], 'difficulty' : session['difficulty']})



# Create your views here.
