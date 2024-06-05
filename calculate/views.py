from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView

from .forms import BPForm

# Create your views here.
# ホーム画面
class HomeView(View):
    template_name = 'calculate/home.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

# 平均血圧計算画面
class BPView(FormView):
    template_name = 'calculate/bp.html'
    form_class = BPForm
    
    def form_valid(self, form):
        systolic_bp_values = form.cleaned_data['systolic_bp'].split()  # 収縮期血圧の値をリストに変換
        diastolic_bp_values = form.cleaned_data['diastolic_bp'].split()  # 拡張期血圧の値をリストに変換
        
        # 文字列を整数に変換
        systolic_bp_values = list(map(int, systolic_bp_values))
        diastolic_bp_values = list(map(int, diastolic_bp_values))

        # 最大の収縮期血圧と最小の拡張期血圧を計算に使用
        max_systolic_bp = max(systolic_bp_values)
        min_diastolic_bp = min(diastolic_bp_values)

        mean_bp = (max_systolic_bp - min_diastolic_bp) / 3 + min_diastolic_bp
        
        context = self.get_context_data()
        context['mean_bp'] = mean_bp
        context['max_systolic_bp'] = max_systolic_bp
        context['min_diastolic_bp'] = min_diastolic_bp
        
        return self.render_to_response(context)
    
    
    
    
    
    
    
    
    
    
    