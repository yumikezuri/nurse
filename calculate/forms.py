from django import forms

class BPForm(forms.Form):
    systolic_bp = forms.CharField(label='収縮期血圧', required=True)
    diastolic_bp = forms.CharField(label='拡張期血圧', required=True)