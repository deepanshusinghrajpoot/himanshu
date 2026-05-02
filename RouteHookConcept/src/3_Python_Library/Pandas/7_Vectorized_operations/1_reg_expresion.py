import numpy as np
import pandas as pd


import os



path_dir = os.path.dirname(__file__)

path_file_titanic = os.path.join(path_dir, '../1_Dataset/titanic.csv')



titanic = pd.read_csv(path_file_titanic)




print(titanic)
'''
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
'''


print(titanic.columns)
'''
Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='str')
'''



titanic['lastname'] = titanic['Name'].str.split(',').str.get(0)
titanic[['title', 'firstname']] = titanic['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True)



# Apply regex
#==============


# Ques : Search johan which contains upper or lower
#...................................................

print(titanic[titanic['firstname'].str.contains('john', case=False)])
'''
     PassengerId  Survived  Pclass  ...   lastname      title                                    firstname
1              2         1       1  ...    Cumings       Mrs.        John Bradley (Florence Briggs Thayer)
41            42         0       2  ...     Turpin       Mrs.  William John Robert (Dorothy Ann Wonnacott)
45            46         0       3  ...     Rogers        Mr.                                 William John
98            99         1       2  ...     Doling       Mrs.                      John T (Ada Julia Bone)
112          113         0       3  ...     Barton        Mr.                                   David John
117          118         0       2  ...     Turpin        Mr.                          William John Robert
160          161         0       3  ...      Cribb        Mr.                                John Hatfield
162          163         0       3  ...  Bengtsson        Mr.                                  John Viktor
165          166         1       3  ...  Goldsmith    Master.                 Frank John William "Frankie"
168          169         0       1  ...    Baumann        Mr.                                       John D
188          189         0       3  ...     Bourke        Mr.                                         John
212          213         0       3  ...     Perkin        Mr.                                   John Henry
226          227         1       2  ...    Mellors        Mr.                                 William John
227          228         0       3  ...     Lovell        Mr.                          John Hall ("Henry")
324          325         0       3  ...       Sage        Mr.                               George John Jr
328          329         1       3  ...  Goldsmith       Mrs.               Frank John (Emily Alice Brown)
401          402         0       3  ...      Adams        Mr.                                         John
418          419         0       2  ...   Matthews        Mr.                                 William John
467          468         0       1  ...      Smart        Mr.                              John Montgomery
527          528         0       1  ...   Farthing        Mr.                                         John
548          549         0       3  ...  Goldsmith        Mr.                                   Frank John
549          550         1       2  ...     Davies    Master.                               John Morgan Jr
550          551         1       1  ...     Thayer        Mr.                              John Borland Jr
563          564         0       3  ...    Simmons        Mr.                                         John
572          573         1       1  ...      Flynn        Mr.                        John Irwin ("Irving")
574          575         0       3  ...       Rush        Mr.                           Alfred George John
581          582         1       1  ...     Thayer       Mrs.      John Borland (Marian Longstreth Morris)
583          584         0       1  ...       Ross        Mr.                                    John Hugo
586          587         0       2  ...     Jarvis        Mr.                                  John Denzil
594          595         0       2  ...    Chapman        Mr.                                   John Henry
613          614         0       3  ...     Horgan        Mr.                                         John
624          625         0       3  ...      Bowen        Mr.                             David John "Dai"
657          658         0       3  ...     Bourke       Mrs.                             John (Catherine)
694          695         0       1  ...       Weir       Col.                                         John
698          699         0       1  ...     Thayer        Mr.                                 John Borland
700          701         1       1  ...      Astor       Mrs.        John Jacob (Madeleine Talmadge Force)
733          734         0       2  ...   Berriman        Mr.                                 William John
760          761         0       3  ...   Garfirth        Mr.                                         John
765          766         1       1  ...   Hogeboom       Mrs.                        John C (Anna Andrews)
818          819         0       3  ...       Holm        Mr.                       John Fredrik Alexander
822          823         0       1  ...   Reuchlin  Jonkheer.                                  John George
825          826         0       3  ...      Flynn        Mr.                                         John
848          849         0       2  ...     Harper       Rev.                                         John
864          865         0       2  ...       Gill        Mr.                                 John William

[44 rows x 15 columns]
'''


# Ques : Find lastname with start and end char vowel

# ^ -> indicate first charactor
# $ -> last charactor
# . -> any charactor
# + -> any number of charactor
# [^a] -> all charactor except a

print(titanic[titanic['lastname'].str.contains('^[aeiouAEIOU].+[aeiouAEIOU]$')])
'''
     PassengerId  Survived  Pclass  ...        lastname title                                 firstname
30            31         0       1  ...       Uruchurtu  Don.                                  Manuel E
49            50         0       3  ...  Arnold-Franchi  Mrs.                  Josef (Josefine Franchi)
207          208         1       3  ...        Albimona   Mr.                             Nassef Cassem
210          211         0       3  ...             Ali   Mr.                                     Ahmed
353          354         0       3  ...  Arnold-Franchi   Mr.                                     Josef
493          494         0       1  ...    Artagaveytia   Mr.                                     Ramon
518          519         1       2  ...           Angle  Mrs.  William A (Florence "Mary" Agnes Hughes)
784          785         0       3  ...             Ali   Mr.                                   William
840          841         0       3  ...        Alhomaki   Mr.                             Ilmari Rudolf

[9 rows x 15 columns]
'''

print(titanic[titanic['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')])
# ^[^aeiouAEIOU] :- mean except all charactor which are not start with aeiouAEIOU
# [^aeiouAEIOU]$ :- mean except all charactor which are not end with aeiouAEIOU

''' 
     PassengerId  Survived  Pclass                                               Name  ... Embarked   lastname  title                              firstname
0              1         0       3                            Braund, Mr. Owen Harris  ...        S     Braund    Mr.                            Owen Harris 
1              2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...        C    Cumings   Mrs.  John Bradley (Florence Briggs Thayer) 
2              3         1       3                             Heikkinen, Miss. Laina  ...        S  Heikkinen  Miss.                                  Laina 
5              6         0       3                                   Moran, Mr. James  ...        Q      Moran    Mr.                                  James 
6              7         0       1                            McCarthy, Mr. Timothy J  ...        S   McCarthy    Mr.                              Timothy J 
..           ...       ...     ...                                                ...  ...      ...        ...    ...                                    ... 
884          885         0       3                             Sutehall, Mr. Henry Jr  ...        S   Sutehall    Mr.                               Henry Jr 
887          888         1       1                       Graham, Miss. Margaret Edith  ...        S     Graham  Miss.                         Margaret Edith 
888          889         0       3           Johnston, Miss. Catherine Helen "Carrie"  ...        S   Johnston  Miss.               Catherine Helen "Carrie" 
889          890         1       1                              Behr, Mr. Karl Howell  ...        C       Behr    Mr.                            Karl Howell 
890          891         0       3                                Dooley, Mr. Patrick  ...        Q     Dooley    Mr.                                Patrick 

[671 rows x 15 columns]
'''




# slicing
#---------

print(titanic['Name'].str[:2])
'''
0      Br
1      Cu
2      He
3      Fu
4      Al
       ..
886    Mo
887    Gr
888    Jo
889    Be
890    Do
Name: Name, Length: 891, dtype: str
'''

print(titanic['Name'].str[::-1])
'''
0                                sirraH newO .rM ,dnuarB
1      )reyahT sggirB ecnerolF( yeldarB nhoJ .srM ,sg...
2                                 aniaL .ssiM ,nenikkieH
3           )leeP yaM yliL( htaeH seuqcaJ .srM ,ellertuF
4                               yrneH mailliW .rM ,nellA
                             ...
886                                sazouJ .veR ,alivtnoM
887                         htidE teragraM .ssiM ,maharG
888             "eirraC" neleH enirehtaC .ssiM ,notsnhoJ
889                                llewoH lraK .rM ,rheB
890                                  kcirtaP .rM ,yelooD
Name: Name, Length: 891, dtype: str
'''

print(titanic['Name'].str[::2])
'''
0                    Ban,M.Oe ars
1      Cmns r.Jh rde Foec rgsTae)
2                     Hiknn is an
3          Ftel,Ms aqe et Ll a el
4                    Aln r ila er
                  ...
886                   Mnvl,Rv uzs
887                Gaa,Ms.Mrae dt
888          Jhso,Ms.CteieHln"are
889                   Bh,M.Kr oel
890                    Doe,M.Ptik
Name: Name, Length: 891, dtype: str
'''

print(titanic['Name'].str[:6:2])
'''
0      Ban
1      Cmn
2      Hik
3      Fte
4      Aln
      ...
886    Mnv
887    Gaa
888    Jhs
889    Bh,
890    Doe
Name: Name, Length: 891, dtype: str
'''