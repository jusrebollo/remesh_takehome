""""
Justin Rebollo 5/7/21
Below you will find my implementation for visualizing the Twitter JSON data
I used pandas to normalize and manipulate the data
To visualize the data interactively I used plotly express with Dash
Thank you for your time!
"""
# import needed packages
import csv
import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

# ignores chained operation warning in pandas
pd.options.mode.chained_assignment = None

# load json data
p = Path(r'data.json')
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

# create a data frame for tweets only , max level handles nesting
df = pd.json_normalize(data, 'tweets', max_level=1)

# normalize data for analysis
# counting the length of each tweet
df['tweet_length'] = df['text'].str.len()

# count the number of hashtags per tweet, counting each hashtag id as one
df['num_hashtags'] = df['hashtags'].str.len()

# count the numner of likes per tweet, counting each hashtag id as one
df['num_likes'] = df['likes'].str.len()

# count the number of retweets for each tweet
# dealing with NaaN values in retweet_id and converting dtype from float to int
df['retweet_id'] = df['retweet_id'].fillna(-1)
df['retweet_id'] = df['retweet_id'].apply(int)


# for loop to count number of retweet ids for each tweet_id
id = []
rt_id = []
id = df['id']
rt_id = df['retweet_id']
count_list = []
i = 0
for i in id:
    count = (df['retweet_id'] == i).sum()
    count_list.append(count)
    i = i+1
    count = 0
# add retweet_count to our df
df['retweet_count'] = count_list

# new dataframe for our visualisation data
df_clean = df[['tweet_length', 'num_hashtags', 'num_likes', 'retweet_count']]

# engagement score = likes + retweets
# implement new column to reflect the engagement score
df_clean['engagement_score'] = df_clean['num_likes'] + df_clean['retweet_count']
df_clean['tweet_score'] = df_clean['tweet_length'] + df_clean['num_hashtags']

# dash visualisation on local host

tweet_length = df_clean['tweet_length']
num_likes = df_clean['num_likes']
num_hashtags = df_clean['num_hashtags']

app = dash.Dash(__name__)

fig0 = px.scatter(df_clean, x="tweet_length", y="num_likes", color = 'engagement_score')

fig1 = px.scatter_matrix(df_clean,dimensions=["tweet_length", "num_hashtags"
    , "num_likes", "retweet_count"],color="engagement_score")

fig2 = px.density_heatmap(df_clean, x="tweet_score", y="engagement_score")

fig3 = px.scatter(df_clean, x="num_hashtags", y="num_likes", color = 'engagement_score')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.Div([
            html.H1(children='Remesh Twitter Data Visualization'),
            html.H2(children='Number of Tweet Likes vs. Tweet Length'),
            html.Div(children='''
               This is a plot displaying the number of tweet likes vs. tweet length 
               across tweets. The engagement score = number of likes + 
               number of retweets. There are two clusters in the dataset. 
               Cluster A encompasses  tweets with ~100 or more likes within 
               a tweet length of ~15 to ~110. While cluster B encompasses tweets
               with less then ~50 likes with tweet length between ~0 and ~240
            '''),

            dcc.Graph(
                id='graph1',
                figure=fig0
            ),
        ], className='six columns'),

        html.Div([
            html.H2(children=' Tweet Likes vs. Number of Hashtags'),
            html.Div(children='''
              This is a plot displaying the number of tweet likes vs number of 
              hastags per tweet. It is evident that the number of hashtags in 
              the range of 2-3 have the most amount of likes compared to the 
              remainder of the dataset. 
           '''),

            dcc.Graph(
                id='graph4',
                figure=fig3
            ),
        ], className='six columns'),


        html.Div([
            html.H2(children='Correlation Matrix of Relevant Parameters'),

            html.Div(children='''
                This is a correlation matrix of tweet_length, num_hashtags, 
                retweet_count, and number of likes. 
            '''),

            dcc.Graph(
                id='graph2',
                figure=fig1
            ),
        ], className='six columns'),

    ], className='row'),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H2(children='Heat Map of Tweet Score vs Engagement Score'),

        html.Div(children='''
                This is a plot of the tweet score vs the engagement score. The
                tweet score = length of the tweet + number of hashtags. Instead 
                of the color differentiation being the engagement score, the 
                color represents the count of each class.  
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig2
        ),
    ], className='row'),
])

if __name__ == '__main__':
    app.run_server(debug=True)