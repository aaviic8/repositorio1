#!C:/Users/zx23student3290/AppData/Local/Programs/Python/Python312/python.exe

import os # sistema operativo 
import urllib.parse # para parsear la query string

print("Content-type: text/html\n")

qs = os.environ.get('QUERY_STRING')

parametros = urllib.parse.parse_qs(qs)

nums1 = int(parametros.get('num1',['0'])[0])
nums2 = int(parametros.get('num2',['0'])[0])

print('''
<!DOCTYPE html>
<html lang="es">
<head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Operaciones basicas</title>
</head>
<body>
        ''')

print('<h1>',nums1, '</h1>')
print('<h1>',nums2, '</h1>')

print('''
</body>
</html>
        '''
        )