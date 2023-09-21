from django import forms

from . import models


class TicketForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["description", "tags"]

    def clean_tags(self):
        tags = self.cleaned_data["tags"]
        for tag in tags:
            if " " in tag:
                raise forms.ValidationError("tags must have'n space ")
        return tags
