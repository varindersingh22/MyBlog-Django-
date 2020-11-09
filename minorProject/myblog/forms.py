from django import forms
from .models import Post,Category,Comment


choices = Category.objects.all().values_list('name','name')

choice_list=[]
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','header_image','body','snippet')
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':"Title here"}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control',}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.TextInput(attrs={'class':'form-control'})
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets ={
            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':"Title here"}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }