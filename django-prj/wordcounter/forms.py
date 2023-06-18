from django import forms


class WordForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(), required=True)
    # attrs={"rows":5, "cols":20}