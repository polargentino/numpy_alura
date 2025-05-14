import pandas as pd

datos_punto_coma = pd.read_csv('superstore_data_punto_coma.csv', sep = ';', nrows = 15)
print(datos_punto_coma) # al usar nrows no tengo que usar.head(), porque sino leería las primeras 5

'''
       Id  Year_Birth   Education Marital_Status  ...  NumStorePurchases  NumWebVisitsMonth  Response Complain
0    1826        1970  Graduation       Divorced  ...                  6                  1         1        0
1       1        1961  Graduation         Single  ...                  7                  5         1        0
2   10476        1958  Graduation        Married  ...                  5                  2         0        0
3    1386        1967  Graduation       Together  ...                  2                  7         0        0
4    5371        1989  Graduation         Single  ...                  2                  7         1        0
5    7348        1958         PhD         Single  ...                  5                  2         1        0
6    4073        1954    2n Cycle        Married  ...                  7                  6         1        0
7    1991        1967  Graduation       Together  ...                  3                  5         0        0
8    4047        1954         PhD        Married  ...                  9                  4         0        0
9    9477        1954         PhD        Married  ...                  9                  4         0        0
10   2079        1947    2n Cycle        Married  ...                 10                  1         0        0
11   5642        1979      Master       Together  ...                  6                  4         0        0
12  10530        1959         PhD          Widow  ...                  6                  1         1        0
13   2964        1981  Graduation        Married  ...                  2                  6         0        0
14  10311        1969  Graduation        Married  ...                  0                  1         0        0

[15 rows x 22 columns]
'''