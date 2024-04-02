from django import forms 
from .models import Comment

class AddCommentForm(forms.ModelForm):
    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols': 100}))
    stars_given=forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model=Comment
        fields=['comment','stars_given']


class CommentUpdateForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}))
    stars_given = forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Comment
        fields = ['comment','stars_given']