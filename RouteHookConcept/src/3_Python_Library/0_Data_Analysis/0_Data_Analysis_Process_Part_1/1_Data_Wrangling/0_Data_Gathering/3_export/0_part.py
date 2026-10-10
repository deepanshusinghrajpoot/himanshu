

import pandas as pd


import os



path = os.path.dirname(__file__)

path_file_deliveries = os.path.join(path, '../../../../../Pandas/1_Dataset/deliveries.csv')

ipl = pd.read_csv(path_file_deliveries)



print(ipl)
'''
        match_id  inning         batting_team                 bowling_team  over  ...  extra_runs total_runs player_dismissed dismissal_kind    fielder
0              1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          0              NaN            NaN        NaN      
1              1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          0              NaN            NaN        NaN      
2              1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          4              NaN            NaN        NaN      
3              1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           0          0              NaN            NaN        NaN      
4              1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1  ...           2          2              NaN            NaN        NaN      
...          ...     ...                  ...                          ...   ...  ...         ...        ...              ...            ...        ...      
179073     11415       2  Chennai Super Kings               Mumbai Indians    20  ...           0          1              NaN            NaN        NaN      
179074     11415       2  Chennai Super Kings               Mumbai Indians    20  ...           0          2              NaN            NaN        NaN      
179075     11415       2  Chennai Super Kings               Mumbai Indians    20  ...           0          1        SR Watson        run out  KH Pandya      
179076     11415       2  Chennai Super Kings               Mumbai Indians    20  ...           0          2              NaN            NaN        NaN      
179077     11415       2  Chennai Super Kings               Mumbai Indians    20  ...           0          0        SN Thakur            lbw        NaN      

[179078 rows x 21 columns]
'''


print(ipl.info())
'''
<class 'pandas.DataFrame'>
RangeIndex: 179078 entries, 0 to 179077
Data columns (total 21 columns):
 #   Column            Non-Null Count   Dtype
---  ------            --------------   -----
 0   match_id          179078 non-null  int64
 1   inning            179078 non-null  int64
 2   batting_team      179078 non-null  str
 3   bowling_team      179078 non-null  str
 4   over              179078 non-null  int64
 5   ball              179078 non-null  int64
 6   batsman           179078 non-null  str
 7   non_striker       179078 non-null  str
 8   bowler            179078 non-null  str
 9   is_super_over     179078 non-null  int64
 10  wide_runs         179078 non-null  int64
 11  bye_runs          179078 non-null  int64
 12  legbye_runs       179078 non-null  int64
 13  noball_runs       179078 non-null  int64
 14  penalty_runs      179078 non-null  int64
 15  batsman_runs      179078 non-null  int64
 16  extra_runs        179078 non-null  int64
 17  total_runs        179078 non-null  int64
 18  player_dismissed  8834 non-null    str
 19  dismissal_kind    8834 non-null    str
 20  fielder           6448 non-null    str
dtypes: int64(13), str(8)
memory usage: 28.7 MB
None
'''



df = pd.DataFrame()

# df.to : After to you are see all build export method




# to_csv
#--------


print(ipl.groupby('batsman')['batsman_runs'].sum().reset_index())
'''
            batsman  batsman_runs
0    A Ashish Reddy           280
1        A Chandila             4
2          A Chopra            53
3       A Choudhary            25
4       A Dananjaya             4
..              ...           ...
511     YV Takawale           192
512   Yashpal Singh            47
513     Younis Khan             3
514    Yuvraj Singh          2765
515          Z Khan           117

[516 rows x 2 columns]
'''

path_to_save_batsman_runs = os.path.join(path, '../4_save_export_file/batsman_runs.csv')
ipl.groupby('batsman')['batsman_runs'].sum().reset_index().to_csv(path_to_save_batsman_runs, index=False)

path_to_save_batsman_runs_bowling_team = os.path.join(path, '../4_save_export_file/batsman_runs_bowling_team.csv')
ipl.pivot_table(index='batsman', columns='bowling_team', values='batsman_runs', aggfunc='sum').to_csv(path_to_save_batsman_runs_bowling_team)






# to_excel
#----------


path_to_save_batsman_runs = os.path.join(path, '../4_save_export_file/batsman_runs.xlsx')
ipl.groupby('batsman')['batsman_runs'].sum().reset_index().to_excel(path_to_save_batsman_runs, index=False)

path_to_save_batsman_runs_bowling_team = os.path.join(path, '../4_save_export_file/batsman_runs_bowling_team.xlsx')
ipl.pivot_table(index='batsman', columns='bowling_team', values='batsman_runs', aggfunc='sum').to_excel(path_to_save_batsman_runs_bowling_team)




# How to store mupltiple excel sheet
#....................................

path_to_save_output_xlsx = os.path.join(path, '../4_save_export_file/output.xlsx')

temp_df_1 = ipl.groupby('batsman')['batsman_runs'].sum().reset_index()
temp_df_2 = ipl.pivot_table(index='batsman', columns='bowling_team', values='batsman_runs', aggfunc='sum')


with pd.ExcelWriter(path_to_save_output_xlsx) as writer:
    temp_df_1.to_excel(writer, sheet_name='Sheet_name_1')
    temp_df_2.to_excel(writer, sheet_name='Sheet_name_2')

print(temp_df_2.info())
print(temp_df_2)






# to_html
#---------

path_to_save_sixes_heatmap = os.path.join(path, '../4_save_export_file/sixes_heatmap.html')
ipl[ipl['batsman_runs']==6].pivot_table(index='over', columns='ball', values='batsman_runs', aggfunc='count').to_html(path_to_save_sixes_heatmap)






# to_json
#---------

print(ipl.groupby(['batting_team', 'batsman'])['batsman_runs'].sum())
'''
batting_team         batsman
Chennai Super Kings  A Flintoff               62
                     A Mukund                  0
                     A Nehra                   1
                     AS Rajpoot                2
                     AT Rayudu               910
                                            ...
Sunrisers Hyderabad  WP Saha                 223
                     X Thalaivan Sargunam     10
                     Y Venugopal Rao          71
                     YK Pathan               319
                     Yuvraj Singh            488
Name: batsman_runs, Length: 935, dtype: int64
'''



print(ipl.groupby(['batting_team', 'batsman'])['batsman_runs'].sum().unstack())
'''
batsman                      A Ashish Reddy  ...  Z Khan
batting_team                                 ...
Chennai Super Kings                     NaN  ...     NaN
Deccan Chargers                        35.0  ...     NaN
Delhi Capitals                          NaN  ...     NaN
Delhi Daredevils                        NaN  ...    10.0
Gujarat Lions                           NaN  ...     NaN
Kings XI Punjab                         NaN  ...     NaN
Kochi Tuskers Kerala                    NaN  ...     NaN
Kolkata Knight Riders                   NaN  ...     NaN
Mumbai Indians                          NaN  ...    40.0
Pune Warriors                           NaN  ...     NaN
Rajasthan Royals                        NaN  ...     NaN
Rising Pune Supergiant                  NaN  ...     NaN
Rising Pune Supergiants                 NaN  ...     NaN
Royal Challengers Bangalore             NaN  ...    67.0
Sunrisers Hyderabad                   245.0  ...     NaN

[15 rows x 516 columns]
'''


path_to_save_ipl = os.path.join(path, '../4_save_export_file/ipl.json')
ipl.groupby(['batting_team', 'batsman'])['batsman_runs'].sum().unstack().to_json(path_to_save_ipl)





# to_sql
#--------
# to_sql({table_name}, con=engine, if_exists='append')


import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost/ipl')
# {root}:{password}@{url}/{database}

ipl.to_sql('ipl_delivery', con=engine, if_exists='replace')
ipl.groupby('batsman')['batsman_runs'].sum().reset_index().to_sql('batsman_runs', con=engine, if_exists='replace')
ipl[ipl['batsman_runs']==6].pivot_table(index='over', columns='ball', values='batsman_runs', aggfunc='count').to_sql('six_hitmap', con=engine, if_exists='replace')

# if_exists
#...........
# 'append'
# 'delete_row'
# 'fail'
# 'replace'



