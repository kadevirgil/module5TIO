from django import forms 

from .models import Review

# class ReviewForm(forms.Form): 
#     username = forms.CharField(label="Name", max_length=50)
#     email = forms.CharField(label="Email", widget=forms.EmailInput)
#     feedback = forms.CharField(label="Feedback", widget=forms.Textarea) # This creates a char field similar to the <textarea> HTML tag
    
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'username': "Your Name",
            'email': "Your Email",
            'feedback': "Your Feeback"
        }
        
        error_messages = {
            'username': {
                'required': 'Your name must not be empty',
                'max_length': 'Your name must not be longer than 100 characters'
            },
            'feedback': {
                'max_length': 'Your feedback must not be longer than 200 characters'
            }
        }
        
        