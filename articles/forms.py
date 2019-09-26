from django import forms


# 사용자가 입력하는 값만 작성 
class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the title...',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter the content...',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    