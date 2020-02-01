from django.urls import path
from . import views
urlpatterns = [
	path("",views.index, name="Home"),


	path("trilingo",views.trilingo, name="trilango"),
	path("tribalmatrimony",views.tribalmatrimony, name="tribalmatrimony"),
	path("toungestop",views.toungestop, name="toungestop"),
	path("mundaDhaba",views.mundaDhaba, name="mundaDhaba"),
	path("jharkhandmatrimony",views.jharkhandmatrimony, name="jharkhandmatrimony"),	

	path("services",views.services, name="services"),
	path("internship",views.internship, name="internship"),
	path("about",views.about, name="about"),
	path("philosophy",views.philosophy, name="philosophy"),
	path("portfolio",views.portfolio, name="portfolio"),
	path("contact",views.contact, name="contact"),
	path("research",views.research, name="research"),
	path("community",views.community, name="community"),

	path("team",views.team, name="team"),
	path("career",views.career, name="career"),

	path("apply",views.apply, name="apply"),
	path("intern_frontend",views.intern_frontend, name="intern_frontend"),
	path("intern_backend",views.intern_backend, name="intern_backend"),
	path("intern_datascience",views.intern_datascience, name="intern_datascience"),
	path("intern_linguist",views.intern_linguist, name="intern_linguist"),
	path("intern_design",views.intern_design, name="intern_design"),
	path("team_productengineering",views.team_productengineering, name="team_productengineering"),
	path("team_datascience",views.team_datascience, name="team_datascience"),
	path("team_strategyoperation",views.team_strategyoperation, name="team_strategyoperation"),
	path("team_research",views.team_research, name="team_research"),

	
	path("volunteer_culture",views.volunteer_culture, name="volunteer_culture"),
	path("volunteer_justice",views.volunteer_justice, name="volunteer_justice"),
	path("volunteer_language",views.volunteer_language, name="volunteer_language"),
	path("volunteer_society",views.volunteer_society, name="volunteer_society"),
	
	
]
