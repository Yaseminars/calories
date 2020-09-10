from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from .models import usedCalories, Nutzer

USER_CHOICES= [
    ('user1', 'User1'),
    ('user2', 'User2'),
    ]
class WeightForm(forms.Form):
    weight = forms.IntegerField(
        widget= forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Gewicht',
            'type': 'number',
            'pattern': '\d*'
            }),
        label = 'Gewicht',
        required=True
    )
    loseWeight = forms.IntegerField(
        widget= forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Gewichtsverlust',
            'type': 'number',
            'pattern': '\d*'
            }),
        label = 'Gewichtsverlust pro Monat',
        required=True
    )



class UserSelect(forms.Form):
    user = forms.CharField(
        label='User wählen:',
        widget=forms.RadioSelect(attrs={'onchange': 'changed(this);'},choices=USER_CHOICES))

MealsFormset = inlineformset_factory(
    Nutzer,
    usedCalories,
    extra=1,
    fields=('Mahlzeit', 'Kilokalorien')
)
