from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Your tweet', 'class': 'form-control'}))
    class Meta:
        model = Tweet
        fields = [
            #'user',
            'content'
        ]
        #exclude = ['user']

    # def clean_content(self, *args, **kwargs):
    #     content = 'abc'
    #     if content == 'abc':
    #         raise forms.ValidationError('Cannot be abc')
    #     return content