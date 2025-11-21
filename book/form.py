from django import forms
from book.models import Author


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50, label='عنوان', widget=forms.TextInput(attrs={ 'class':'form-control mt-2'}))
    description = forms.CharField(max_length=255, label='توضیحات', widget=forms.Textarea(attrs={ 'class':'form-contri mt-2'}))
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            forms.ValidationError("کوچیکه")
        return name


class AuthorForm(forms.ModelForm):
    class Meta :
        model = Author
        fields = ['first_name','last_name','birthdate','biografi']




