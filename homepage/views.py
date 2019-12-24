from django.views.generic import TemplateView

<<<<<<< HEAD
class HomePageView(TemplateView):
    template_name = 'home.html'
=======

def home(request):
    return render(request,"homepage/minipo/index-5.html")
>>>>>>> 94ba12da256e47b63603e53d293fc206ec296a56
