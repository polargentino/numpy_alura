'''
Explicación del Código:
Importar las bibliotecas necesarias:

import pandas as pd: Importa la biblioteca pandas para manipulación y análisis de datos.
import requests: Importa la biblioteca requests para hacer solicitudes HTTP.
import json: Importa el módulo json para manejar datos JSON.

Obtener los datos de la API:

datos_frutas = requests.get('https://fruityvice.com/api/fruit/all'): Realiza una solicitud GET a la 
API de Fruitvice para obtener datos de todas las frutas.

Convertir la respuesta a JSON:

resultado = json.loads(datos_frutas.text): Convierte el texto de la respuesta en un objeto JSON.

Normalizar el JSON completo:

datos_frutas_normalizado = pd.json_normalize(resultado): Normaliza el objeto JSON en un DataFrame de 
pandas, expandiendo la columna nutritions en columnas separadas.

Imprimir el DataFrame normalizado:

print(datos_frutas_normalizado): Imprime el DataFrame normalizado, que ahora incluye columnas 
separadas para cada valor nutricional.

Salida Esperada:

El DataFrame normalizado tendrá columnas separadas para cada valor nutricional, 
como nutritions.carbohydrates, nutritions.protein, nutritions.fat, nutritions.calories, y 
nutritions.sugar. Esto facilita el análisis y la manipulación de los datos.

Con estos pasos, el DataFrame resultante tendrá todas las informaciones nutricionales separadas, lo 
que permite un análisis más detallado y específico de los datos.
'''

import pandas as pd
import requests
import json

# Obtener los datos de la API Fruitvice
datos_frutas = requests.get('https://fruityvice.com/api/fruit/all')

# Convertir la respuesta a JSON
resultado = json.loads(datos_frutas.text)

# Normalizar el JSON completo
datos_frutas_normalizado = pd.json_normalize(resultado)

# Imprimir el DataFrame normalizado
print(datos_frutas_normalizado)

'''
                  name   id           family  ... nutritions.sugar nutritions.carbohydrates  nutritions.protein
0            Persimmon   52        Ebenaceae  ...            18.00                    18.00                0.00
1           Strawberry    3         Rosaceae  ...             5.40                     5.50                0.80
2               Banana    1         Musaceae  ...            17.20                    22.00                1.00
3               Tomato    5       Solanaceae  ...             2.60                     3.90                0.90
4                 Pear    4         Rosaceae  ...            10.00                    15.00                0.40
5               Durian   60        Malvaceae  ...             6.75                    27.10                1.50
6           Blackberry   64         Rosaceae  ...             4.50                     9.00                1.30
7          Lingonberry   65        Ericaceae  ...             5.74                    11.30                0.75
8                 Kiwi   66    Actinidiaceae  ...             9.00                    15.00                1.10
9               Lychee   67      Sapindaceae  ...            15.00                    17.00                0.80
10           Pineapple   10     Bromeliaceae  ...             9.85                    13.12                0.54
11                 Fig   68         Moraceae  ...            16.00                    19.00                0.80
12          Gooseberry   69  Grossulariaceae  ...             0.00                    10.00                0.90
13        Passionfruit   70   Passifloraceae  ...            11.20                    22.40                2.20
14                Plum   71         Rosaceae  ...             9.92                    11.40                0.70
15              Orange    2         Rutaceae  ...             8.20                     8.30                1.00
16          GreenApple   72         Rosaceae  ...             6.40                     3.10                0.40
17           Raspberry   23         Rosaceae  ...             4.40                    12.00                1.20
18          Watermelon   25    Cucurbitaceae  ...             6.00                     8.00                0.60
19               Lemon   26         Rutaceae  ...             2.50                     9.00                1.10
20               Mango   27    Anacardiaceae  ...            13.70                    15.00                0.82
21           Blueberry   33         Rosaceae  ...             5.40                     5.50                0.00
22               Apple    6         Rosaceae  ...            10.30                    11.40                0.30
23               Guava   37        Myrtaceae  ...             9.00                    14.00                2.60
24             Apricot   35         Rosaceae  ...             3.20                     3.90                0.50
25               Melon   41    Cucurbitaceae  ...             8.00                     8.00                0.00
26           Tangerine   77         Rutaceae  ...             9.10                     8.30                0.00
27            Pitahaya   78        Cactaceae  ...             3.00                     7.00                1.00
28                Lime   44         Rutaceae  ...             1.70                     8.40                0.30
29         Pomegranate   79       Lythraceae  ...            13.70                    18.70                1.70
30         Dragonfruit   80        Cactaceae  ...             8.00                     9.00                9.00
31               Grape   81         Vitaceae  ...            16.00                    18.10                0.72
32               Morus   82         Moraceae  ...             8.10                     9.80                1.44
33              Feijoa   76        Myrtaceae  ...             3.00                     8.00                0.60
34             Avocado   84        Lauraceae  ...             0.66                     8.53                2.00
35           Kiwifruit   85    Actinidiaceae  ...             8.90                    14.60                1.14
36           Cranberry   87        Ericaceae  ...             4.00                    12.20                0.40
37              Cherry    9         Rosaceae  ...             8.00                    12.00                1.00
38               Peach   86         Rosaceae  ...             8.40                     9.50                0.90
39           Jackfruit   94         Moraceae  ...            19.10                    23.20                1.72
40        Horned Melon   95    Cucurbitaceae  ...             0.50                     7.56                1.78
41            Hazelnut   96       Betulaceae  ...             4.30                    17.00               15.00
42              Pomelo   98         Rutaceae  ...             8.50                     9.67                0.82
43          Mangosteen   99       Clusiaceae  ...            16.11                    17.91                0.41
44             Pumpkin  100    Cucurbitaceae  ...             3.30                     4.60                1.10
45  Japanese Persimmon  101        Ebenaceae  ...            13.00                    19.00                0.60
46              Papaya   42       Caricaceae  ...             4.40                     5.80                0.50
47              Annona  103       Annonaceae  ...             3.40                    19.10                1.50
48   Ceylon Gooseberry  104       Salicaceae  ...             8.10                     9.60                1.20

[49 rows x 10 columns]
'''

