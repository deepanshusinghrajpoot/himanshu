

import pandas as pd

import os


path = os.path.dirname(__file__)

path_file_medical = os.path.join(path, '../../../../../Pandas/1_Dataset/medical.json')



print(pd.read_json(path_file_medical))
'''
    patient_id  age  gender        disease        hospital  treatment_cost  days_admitted
0            1   45    Male       Diabetes          Apollo           12000              5
1            2   33  Female         Asthma  Max Healthcare            8000              3
2            3   56    Male  Heart Disease           AIIMS           42000             10
3            4   29  Female            Flu   City Hospital            3000              2
4            5   61    Male   Hypertension   Care Hospital           15000              6
..         ...  ...     ...            ...             ...             ...            ...
95          96   41  Female       Diabetes          Apollo           11600              4
96          97   52    Male  Heart Disease           AIIMS           38500              8
97          98   36  Female         Asthma  Max Healthcare            7700              3
98          99   46    Male   Hypertension   Care Hospital           13900              5
99         100   28  Female            Flu   City Hospital            2500              2

[100 rows x 7 columns]
'''


# How to get data from server
#-------------------------------

print(pd.read_json("https://jsonplaceholder.typicode.com/users"))
'''
   id                      name          username  ...                  phone        website                                            company
0   1             Leanne Graham              Bret  ...  1-770-736-8031 x56442  hildegard.org  {'name': 'Romaguera-Crona', 'catchPhrase': 'Mu...
1   2              Ervin Howell         Antonette  ...    010-692-6593 x09125  anastasia.net  {'name': 'Deckow-Crist', 'catchPhrase': 'Proac...
2   3          Clementine Bauch          Samantha  ...         1-463-123-4447    ramiro.info  {'name': 'Romaguera-Jacobson', 'catchPhrase': ...
3   4          Patricia Lebsack          Karianne  ...      493-170-9623 x156       kale.biz  {'name': 'Robel-Corkery', 'catchPhrase': 'Mult...
4   5          Chelsey Dietrich            Kamren  ...          (254)954-1289   demarco.info  {'name': 'Keebler LLC', 'catchPhrase': 'User-c...
5   6      Mrs. Dennis Schulist  Leopoldo_Corkery  ...   1-477-935-8478 x6430        ola.org  {'name': 'Considine-Lockman', 'catchPhrase': '...
6   7           Kurtis Weissnat      Elwyn.Skiles  ...           210.067.6132       elvis.io  {'name': 'Johns Group', 'catchPhrase': 'Config...
7   8  Nicholas Runolfsdottir V     Maxime_Nienow  ...      586.493.6943 x140   jacynthe.com  {'name': 'Abernathy Group', 'catchPhrase': 'Im...
8   9           Glenna Reichert          Delphine  ...   (775)976-6794 x41206     conrad.com  {'name': 'Yost and Sons', 'catchPhrase': 'Swit...
9  10        Clementina DuBuque    Moriah.Stanton  ...           024-648-3804    ambrose.net  {'name': 'Hoeger LLC', 'catchPhrase': 'Central...

[10 rows x 8 columns]
'''