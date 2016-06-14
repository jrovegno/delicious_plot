
# coding: utf-8
'''
Convert 
'''
import pandas as pd

def vbar(s):
      return '|' + '|'.join(str(s).split(',')) + '|'

df = pd.read_csv('delicious.csv')

colnames = {'href':'t_link.f_url', 
            'note':'t_link.f_description', 'private':'t_link.f_private', 
            'tags':'t_link.f_tags', 'title':'t_link.f_title', 
            'Unnamed: 0': 't_link.id'}

df.rename(columns=colnames, inplace=True)

df['t_link.f_add_date'] = pd.to_datetime(df.add_date, unit='s')
df.drop('add_date', axis=1, inplace=True)
df.dropna(subset=['t_link.f_url', 't_link.f_private'], inplace=True)
df['t_link.f_private'] = df['t_link.f_private'].astype(bool)
df['t_link.f_tags'] = df[['t_link.f_tags']].applymap(vbar)

df.to_csv('db.csv', index=False)
