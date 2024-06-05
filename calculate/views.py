from django.shortcuts import render
from django.views import View

# Create your views here.
# ホーム画面
class HomeView(View):
    template_name = 'calculate/home.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)