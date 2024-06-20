from django import forms 

class ReviewForm(forms.Form): 
    username = forms.CharField(label="Name", max_length=50)
    email = forms.EmailField()
    feedback = forms.CharField() 
    
