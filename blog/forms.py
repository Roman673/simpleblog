from django.forms import ModelForm, Textarea

from .models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': '',}
        widgets = {'text': Textarea(attrs={'cols': 20, 'rows': 3}),}