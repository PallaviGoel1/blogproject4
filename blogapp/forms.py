from django import forms
from .models import Post, Comment, Category
from django_summernote.widgets import SummernoteWidget

# Apply summernote to specific fields.    
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            #'slug' : forms.TextInput(attrs={'class':'form-control'}),
            
            'author' : forms.TextInput(attrs={'class':'form-control','value':'', 'id': 'elder'}),
            #'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body' : SummernoteWidget(),
            #'body' :  forms.TextField(),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
           # 'slug' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')