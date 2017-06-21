from django import forms

class CompForm(forms.Form):

	INSTITUTIONS = (
		('icmc', 'USP - Intituto de Ciências Matemáticas e de Computação'),
		('ime', 'USP - Instituto de Matemática e Estátistica'),
		('ufrgs', 'UFRGS - Universidade Federal do Rio Grande do Sul')
    )

	COURSES = (
		('bcc', 'Ciências de Computação'),
		('bsi', 'Sistemas de Informação'),
		('eng', 'Engenharia de Computação')
	)

	inst1 = forms.ChoiceField(label='Instituição', widget=forms.Select, choices=INSTITUTIONS)
	inst2 = forms.ChoiceField(label='Instituição', widget=forms.Select, choices=INSTITUTIONS)
	curso1 = forms.ChoiceField(label='Curso', widget=forms.Select, choices=COURSES)
	curso2 = forms.ChoiceField(label='Curso', widget=forms.Select, choices=COURSES)