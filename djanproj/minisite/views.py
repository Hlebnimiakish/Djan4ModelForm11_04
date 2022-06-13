from django.shortcuts import render, redirect
from django.views import View

from minisite.forms import CustomerForm

class HomepageView(View):
    def get(self, request):
        return render(request, 'home.html', {})


class AddingFormView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'formadding.html', {'form': form})
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')
