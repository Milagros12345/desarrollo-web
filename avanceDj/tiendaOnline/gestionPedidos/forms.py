from django import forms

class formularioContacto(forms.Form):
    asunto=forms.CharField() #que ausnto va ser una letra
    email=forms.EmailField() #va ser un campo de correo electronico
    mensaje=forms.CharField()

