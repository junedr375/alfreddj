from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home/index.html')

###################################################################

def trilingo(request):
	return render(request, 'home/trilingo.html')

def tribalmatrimony(request):
	return render(request, 'home/tribalmatrimony.html')

def toungestop(request):
	return render(request, 'home/toungestop.html')

def mundaDhaba(request):
	return render(request, 'home/mundaDhaba.html')

def jharkhandmatrimony(request):
	return render(request, 'home/jharkhandmatrimony.html')

####################################################################


def services(request):
	return render(request, 'home/services.html')

def internship(request):
	return render(request, 'home/internship.html')

def about(request):
	return render(request, 'home/about.html')

def philosophy(request):
	return render(request, 'home/philosophy.html')

def portfolio(request):
	return render(request, 'home/portfolio.html')

def contact(request):
	return render(request, 'home/contact.html')

def research(request):
	return render(request, 'home/research.html')

def community(request):
	return render(request, 'home/community.html')

###################################################################

def team(request):
	return render(request, 'home/team.html')

def career(request):
	return render(request, 'home/career.html')


####################################################################


def apply(request):
	return render(request, 'home/apply.html')

def intern_frontend(request):
	return render(request, 'home/intern_frontend.html')

def intern_backend(request):
	return render(request, 'home/intern_backend.html')

def intern_datascience(request):
	return render(request, 'home/intern_datascience.html')

def intern_linguist(request):
	return render(request, 'home/intern_linguist.html')

def intern_design(request):
	return render(request, 'home/intern_design.html')



def team_productengineering(request):
	return render(request, 'home/team_productengineering.html')

def team_datascience(request):
	return render(request, 'home/team_datascience.html')

def team_strategyoperation(request):
	return render(request, 'home/team_strategyoperation.html')

def team_research(request):
	return render(request, 'home/team_research.html')




def volunteer_culture(request):
	return render(request, 'home/volunteer_culture.html')

def volunteer_justice(request):
	return render(request, 'home/volunteer_justice.html')

def volunteer_language(request):
	return render(request, 'home/volunteer_language.html')

def volunteer_society(request):
	return render(request, 'home/volunteer_society.html')


#################################################################





