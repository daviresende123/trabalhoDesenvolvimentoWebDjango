from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrarForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Traduzindo os rótulos dos campos
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de senha'

        # Traduzindo as mensagens de ajuda
        self.fields['username'].help_text = 'Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.'
        self.fields['password1'].help_text = (
            'Sua senha não pode ser muito parecida com suas outras informações pessoais.<br>'
            'Sua senha deve conter pelo menos 8 caracteres.<br>'
            'Sua senha não pode ser uma senha comumente usada.<br>'
            'Sua senha não pode ser inteiramente numérica.'
        )
        self.fields['password2'].help_text = 'Digite a mesma senha anterior, para verificação.'

        # Traduzindo as mensagens de erro
        self.fields['username'].error_messages = {
            'required': 'Este campo é obrigatório.',
            'max_length': 'Este campo deve ter no máximo 150 caracteres.',
            'invalid': 'Use apenas letras, dígitos e @/./+/-/_.',
        }
        self.fields['password1'].error_messages = {
            'required': 'Este campo é obrigatório.',
            'password_too_short': 'A senha deve conter pelo menos 8 caracteres.',
            'password_too_common': 'Esta senha é muito comum.',
            'password_entirely_numeric': 'A senha não pode ser inteiramente numérica.',
        }
        self.fields['password2'].error_messages = {
            'required': 'Este campo é obrigatório.',
            'password_mismatch': 'As senhas não coincidem.',
        }