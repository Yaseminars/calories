from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import date
from .forms import *
from .models import usedCalories, Nutzer
#from .forms import *
#from .models import *
# Create your views here.
MAX_CAL = 2500

class UserSelectView(TemplateView):
    template = 'kalorienzaehler/userselect.html'
    def get(self,request):
        form = UserSelect()
        args = {
            'form': form
        }
        return render(request,self.template, args)
    def post(self,request):

        return render(request,self.template, args)


class HomeView(TemplateView):
    template_home = 'kalorienzaehler/home.html'
    def get(self,request, username):
        user = username
        today = date.today()
        userID = Nutzer.objects.filter(username=user).first()
        caloriesLeft = userID.maxCalories
        userID = userID.id
        todaysMeals = usedCalories.objects.filter(date=today, user=userID)


        userquery = Nutzer.objects.get(pk=userID)
        formset = MealsFormset(instance=userquery)

        for meal in todaysMeals:
            caloriesLeft = caloriesLeft - meal.Kilokalorien
        message = None
        if caloriesLeft <= 0:
            message = "Tagesbedarf erreicht!"
        args = {
            'formset':formset,
            'message': message,
            'user': user,
            'caloriesLeft': caloriesLeft
        }
        return render(request, self.template_home, args)
    def post(self,request,username):
        today = date.today()
        userID = Nutzer.objects.filter(username=username).first()
        caloriesLeft = userID.maxCalories
        userID = userID.id
        todaysMeals = usedCalories.objects.filter(date=today, user=userID)

        for meal in todaysMeals:
            caloriesLeft = caloriesLeft - meal.Kilokalorien
        userquery = Nutzer.objects.get(pk=userID)
        formset = MealsFormset(request.POST,instance=userquery)
        if formset.is_valid():
            formset.save()

            return HttpResponseRedirect(self.request.path_info)

        message = None
        if caloriesLeft <= 0:
            message = "Tagesbedarf erreicht!"
        args = {
            'formset':formset,
            'message': message,
            'user': user,
            'caloriesLeft': caloriesLeft
        }
        return render(request, self.template_home, args)
        return render(request,self.template_home, args)
