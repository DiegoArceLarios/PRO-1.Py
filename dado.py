import random
response = 'y'


while response == 'y':
    dado = random.randint(1,6)
    if dado == 1:
        print('[    |-   ]')
        print('[    |    ]')
        print('[    |    ]')
    if dado == 2:
        print('[    __   ]')
        print('[   |__   ]')
        print('[    __|  ]')
    if dado == 3:
        print('[    __   ]')
        print('[   |_    ]')
        print('[   |__   ]')
    if dado == 4:
        print('[        ]')
        print('[  |__|  ]')
        print('[     |  ]')
    if dado == 5:
        print('[    __   ]')
        print('[   |__   ]')
        print('[    __|  ]')   
    if dado == 6:
        print('[    __   ]')
        print('[   |__   ]')
        print('[   |__|  ]') 
    respuesta = input('¿Quires imprimir otro numero? (y/n)')
    if respuesta == 'y':
        print('ok')
    elif respuesta == 'n':
        break
    else:
        print('no es una respuesta esperada')
        break



