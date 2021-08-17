def options(request):
	session=request.session
	if request.session.get('cookies') is None:
			session['cookies'] = False
			session['wantToPlay'] = False
			session['gameMode'] = False
			session['difficulty'] = False
			session['userIsLogin'] = False

	elif request.method == 'POST':
		if request.POST.get('aceptCookies') :
			session['cookies'] = True
			session['wantToPlay'] = False
			session['gameMode'] = False
			session['difficulty'] = False
			session['userIsLogin'] = False


		elif request.POST.get('wantToPlay') :
			session['wantToPlay'] = True






		elif request.POST.get('fingers') :
			session['gameMode'] = 'fingers'

		elif request.POST.get('electricity') :
			session['gameMode'] = 'electricity'




		elif request.POST.get('easy') :
			session['difficulty'] = 'easy'


		elif request.POST.get('medium') :
			session['difficulty'] = 'medium'


		elif request.POST.get('hard') :
			session['difficulty'] = 'hard'	




		elif request.POST.get('goHome') :
			session['wantToPlay'] = False
			session['gameMode'] = False
			session['difficulty'] = False


		elif request.POST.get('goBackSelectGameMode') :
			session['gameMode'] = False


		elif request.POST.get('goBackSelectDifficulty') :
			session['difficulty'] = False





	return session
		


	



	


		

	
	
	
	