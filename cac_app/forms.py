from django import forms

class CompForm(forms.Form):

	INSTITUTIONS = (
		('Universidade', (
				('icmc',  'USP - Instituto de Ciências Matemáticas e de Computação'),
				('ime',   'USP - Instituto de Matemática e Estátistica'),
				('ufrgs', 'UFRGS - Universidade Federal do Rio Grande do Sul'),
				('ufpe',  'UFPE - Universidade Federal de Pernambuco'),
				('ufpr',  'UFPR - Universidade Federal do Paraná'),
				('unb',   'UnB - Universidade de Brasília'),
				('puc-rio', 'PUC RIO - Pontifícia Universidade Católica do Rio de Janeiro')

			)
		),
		('Referência', (
				('sbc', 'SBC - Sociedade Brasileira de Computação'),
			)
		)
    )

	COURSES = (
		('bcc', 'Ciências de Computação'),
		('bsi', 'Sistemas de Informação'),
		('eng', 'Engenharia de Computação')
	)

	inst1 = forms.ChoiceField(label='Instituição', widget=forms.Select(attrs={'onChange':'change_link()'}), choices=INSTITUTIONS)
	inst2 = forms.ChoiceField(label='Instituição', widget=forms.Select(attrs={'onChange':'change_link()'}), choices=INSTITUTIONS)
	curso1 = forms.ChoiceField(label='Curso', widget=forms.Select(attrs={'onChange':'change_link()'}), choices=COURSES)
	curso2 = forms.ChoiceField(label='Curso', widget=forms.Select(attrs={'onChange':'change_link()'}), choices=COURSES)