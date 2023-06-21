from PySimpleGUI import PySimpleGUI as sg


#Layout definido
sg.theme('LightBlue3')
layout = [
	[sg.Text('Usuário'), sg.Input(key='usuario', size=(25, 2))],
	[sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(25, 2))],
	[sg.Checkbox('Salvar login?')],
	[sg.Button('Entrar')]
]


#Tela/janela a ser validada
janela = sg.Window('Login', layout)


#Leitura de eventos/variáveis dentro do código
while True:
	eventos, valores = janela.read()
	if eventos == sg.WINDOW_CLOSED:
		break
	if eventos == 'Entrar':
		if valores['usuario'] == 'datacoin' and valores['senha'] == 'datacoin':
			print('Canal Datacoin logado!')
		else:
			print('Login não realizado');
