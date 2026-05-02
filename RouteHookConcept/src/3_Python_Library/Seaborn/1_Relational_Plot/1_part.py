

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px





tips = sns.load_dataset('tips')

print(tips)
'''
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]
'''





gap = px.data.gapminder()


print(gap)

'''
          country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
0     Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4
1     Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4
2     Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4
3     Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4
4     Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4
...           ...       ...   ...      ...       ...         ...       ...      ...
1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE      716
1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE      716
1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE      716
1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE      716
1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE      716

[1704 rows x 8 columns]
'''



temp_df = gap[gap['country'] == 'India']

print(temp_df)
'''
    country continent  year  lifeExp         pop    gdpPercap iso_alpha  iso_num
696   India      Asia  1952   37.373   372000000   546.565749       IND      356
697   India      Asia  1957   40.249   409000000   590.061996       IND      356
698   India      Asia  1962   43.605   454000000   658.347151       IND      356
699   India      Asia  1967   47.193   506000000   700.770611       IND      356
700   India      Asia  1972   50.651   567000000   724.032527       IND      356
701   India      Asia  1977   54.208   634000000   813.337323       IND      356
702   India      Asia  1982   56.596   708000000   855.723538       IND      356
703   India      Asia  1987   58.553   788000000   976.512676       IND      356
704   India      Asia  1992   60.223   872000000  1164.406809       IND      356
705   India      Asia  1997   61.765   959000000  1458.817442       IND      356
706   India      Asia  2002   62.879  1034172547  1746.769454       IND      356
707   India      Asia  2007   64.698  1110396331  2452.210407       IND      356
'''








'''

(1). Relational Plot
=====================

. To see the statistical relation between 2 or more variables.
. Bivariate Analysis


Plots under this section
------------------------

(i). Scatter Plot
(ii). Line Plot

'''

# Hellow gpt give all attribute of relational plot and what is its working and how is it use and add other information if required



# Line Plot 
#----------

# sns.lineplot() -> axes level method -> rectangular 
#......................................................

sns.lineplot(data=temp_df, x='year', y='lifeExp')

plt.show()


# sns.relplot() -> figure level method -> square shape
#...............................................

sns.relplot(data=temp_df, x='year', y='lifeExp', kind='line')

plt.show()



# Where are we use figure level method
#--------------------------------------

# As seaborn library recommended to use figure level method







# hue -> style
#--------------

data_df = gap[gap['country'].isin(['India', 'Pakistan', 'China'])]

print(data_df)
'''
       country continent  year  ...    gdpPercap  iso_alpha  iso_num
288      China      Asia  1952  ...   400.448611        CHN      156 
289      China      Asia  1957  ...   575.987001        CHN      156 
290      China      Asia  1962  ...   487.674018        CHN      156 
291      China      Asia  1967  ...   612.705693        CHN      156 
292      China      Asia  1972  ...   676.900092        CHN      156 
293      China      Asia  1977  ...   741.237470        CHN      156 
294      China      Asia  1982  ...   962.421381        CHN      156 
295      China      Asia  1987  ...  1378.904018        CHN      156 
296      China      Asia  1992  ...  1655.784158        CHN      156 
297      China      Asia  1997  ...  2289.234136        CHN      156 
298      China      Asia  2002  ...  3119.280896        CHN      156 
299      China      Asia  2007  ...  4959.114854        CHN      156 
696      India      Asia  1952  ...   546.565749        IND      356 
697      India      Asia  1957  ...   590.061996        IND      356 
698      India      Asia  1962  ...   658.347151        IND      356 
699      India      Asia  1967  ...   700.770611        IND      356 
700      India      Asia  1972  ...   724.032527        IND      356 
701      India      Asia  1977  ...   813.337323        IND      356 
702      India      Asia  1982  ...   855.723538        IND      356 
703      India      Asia  1987  ...   976.512676        IND      356 
704      India      Asia  1992  ...  1164.406809        IND      356 
705      India      Asia  1997  ...  1458.817442        IND      356 
706      India      Asia  2002  ...  1746.769454        IND      356 
707      India      Asia  2007  ...  2452.210407        IND      356 
1164  Pakistan      Asia  1952  ...   684.597144        PAK      586 
1165  Pakistan      Asia  1957  ...   747.083529        PAK      586 
1166  Pakistan      Asia  1962  ...   803.342742        PAK      586 
1167  Pakistan      Asia  1967  ...   942.408259        PAK      586 
1168  Pakistan      Asia  1972  ...  1049.938981        PAK      586 
1169  Pakistan      Asia  1977  ...  1175.921193        PAK      586 
1170  Pakistan      Asia  1982  ...  1443.429832        PAK      586 
1171  Pakistan      Asia  1987  ...  1704.686583        PAK      586 
1172  Pakistan      Asia  1992  ...  1971.829464        PAK      586 
1173  Pakistan      Asia  1997  ...  2049.350521        PAK      586 
1174  Pakistan      Asia  2002  ...  2092.712441        PAK      586 
1175  Pakistan      Asia  2007  ...  2605.947580        PAK      586 

[36 rows x 8 columns]
'''


sns.relplot(data=data_df, x='year', y='lifeExp', hue='country', kind='line')
plt.show()




data_df_1 = gap[gap['country'].isin(['India', 'Brazil', 'Germany'])]

print(data_df_1)

'''
     country continent  year  lifeExp         pop     gdpPercap iso_alpha  iso_num
168   Brazil  Americas  1952   50.917    56602560   2108.944355       BRA       76
169   Brazil  Americas  1957   53.285    65551171   2487.365989       BRA       76
170   Brazil  Americas  1962   55.665    76039390   3336.585802       BRA       76
171   Brazil  Americas  1967   57.632    88049823   3429.864357       BRA       76
172   Brazil  Americas  1972   59.504   100840058   4985.711467       BRA       76
173   Brazil  Americas  1977   61.489   114313951   6660.118654       BRA       76
174   Brazil  Americas  1982   63.336   128962939   7030.835878       BRA       76
175   Brazil  Americas  1987   65.205   142938076   7807.095818       BRA       76
176   Brazil  Americas  1992   67.057   155975974   6950.283021       BRA       76
177   Brazil  Americas  1997   69.388   168546719   7957.980824       BRA       76
178   Brazil  Americas  2002   71.006   179914212   8131.212843       BRA       76
179   Brazil  Americas  2007   72.390   190010647   9065.800825       BRA       76
564  Germany    Europe  1952   67.500    69145952   7144.114393       DEU      276
565  Germany    Europe  1957   69.100    71019069  10187.826650       DEU      276
566  Germany    Europe  1962   70.300    73739117  12902.462910       DEU      276
567  Germany    Europe  1967   70.800    76368453  14745.625610       DEU      276
568  Germany    Europe  1972   71.000    78717088  18016.180270       DEU      276
569  Germany    Europe  1977   72.500    78160773  20512.921230       DEU      276
570  Germany    Europe  1982   73.800    78335266  22031.532740       DEU      276
571  Germany    Europe  1987   74.847    77718298  24639.185660       DEU      276
572  Germany    Europe  1992   76.070    80597764  26505.303170       DEU      276
573  Germany    Europe  1997   77.340    82011073  27788.884160       DEU      276
574  Germany    Europe  2002   78.670    82350671  30035.801980       DEU      276
575  Germany    Europe  2007   79.406    82400996  32170.374420       DEU      276
696    India      Asia  1952   37.373   372000000    546.565749       IND      356
697    India      Asia  1957   40.249   409000000    590.061996       IND      356
698    India      Asia  1962   43.605   454000000    658.347151       IND      356
699    India      Asia  1967   47.193   506000000    700.770611       IND      356
700    India      Asia  1972   50.651   567000000    724.032527       IND      356
701    India      Asia  1977   54.208   634000000    813.337323       IND      356
702    India      Asia  1982   56.596   708000000    855.723538       IND      356
703    India      Asia  1987   58.553   788000000    976.512676       IND      356
704    India      Asia  1992   60.223   872000000   1164.406809       IND      356
705    India      Asia  1997   61.765   959000000   1458.817442       IND      356
706    India      Asia  2002   62.879  1034172547   1746.769454       IND      356
707    India      Asia  2007   64.698  1110396331   2452.210407       IND      356
'''


sns.relplot(data=data_df_1, x='year', y='lifeExp', hue='country', style='continent', size='continent', kind='line')
plt.show()





# facet plot
#-------------

# facet plot work only with figure level function(work with relplot)
# gpt give all important information about facet plot


sns.relplot(data=tips, x='total_bill', y='tip', col='sex', row='smoker', kind='scatter')

plt.show()





# col wrap
#----------

sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter')
plt.show()


sns.relplot(data=gap, x='lifeExp', y='gdpPercap', col='year',  kind='scatter', col_wrap=3)
plt.show()