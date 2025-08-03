from django import  forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100,label='Поиск',
                             required=False,
                             widget=forms.TextInput(attrs={'class':'form-control search-input',
                                                           'placeholder':'🔍 Поиск',
                                                           'aria-label':'Поиск','type':'search'}))