import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as mp
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] =np.where(df['weight']/(df['height']/100)**2>25,1,0)

var=['cholesterol','gluc']

def fun1(y):
    
    if y == 1:
        return 0
    elif y == 0:
        
        return 0
    else:
        return 1


for x in var:
    
    # df[var]=list(map(fun1,df[var]))
    
    df[x]=df[x].apply(fun1) 

# df_clean=df.query(" ap_lo <= ap_hi")  
# val1=float(df['height'].quantile(0.025))
# val2=float(df['height'].quantile(0.975))
# val3=float(df['weight'].quantile(0.025))
# val4=float(df['weight'].quantile(0.975))
# df_clean=df_clean.query(" height >= @val1 and  height <= @val2 and weight>=@val3 and weight<=@val4 ")
# df=df_clean
# pd.crosstab(df['overweight'],df['cardio'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  
    df_cat = df.melt(id_vars = ["cardio"], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')

    # Draw the catplot with 'sns.catplot()'
    fig=sns.catplot(x='variable',y='total',hue='value',col='cardio',data=df_cat,kind='bar').fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_clean=df.query(" ap_lo <= ap_hi") 
    val1=float(df['height'].quantile(0.025))
    val2=float(df['height'].quantile(0.975))
    val3=float(df['weight'].quantile(0.025))
    val4=float(df['weight'].quantile(0.975))
    df_heat = df_clean.query(" height >= @val1 and  height <= @val2 and weight>=@val3 and weight<=@val4 ")

    # Calculate the correlation matrix
    corr =df_heat.corr().round(1)
    # print(corr)
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10,10)) 
    ax =sns.heatmap(corr, annot=True, mask=mask,fmt='.1f')
    
    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()

# print(actual)
# print( ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1'] ) 
