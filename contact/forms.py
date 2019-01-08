from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=200, required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Mi nombre'}
    ))
    email = forms.EmailField(label='Correo', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'ejemplo@mail.com'}
    ))
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':'3', 'placeholder':'Escribe tu mensaje'}
    ))