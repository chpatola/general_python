import seaborn as sns
from matplotlib import pyplot
from pandas.plotting import scatter_matrix

#***FUNCTIONS TO USE ON SPECIFIC COLUMNS IN DATA**

#Make boxplot of x and y
def boxP(df,xdata,ydata):
    sns.boxplot(x=xdata, y=ydata, data=df)

#Make Regression line plot
def regP(xdata,ydata):
    sns.regplot(x=xdata, y=ydata)
    pyplot.show()

#Make scatterplot of x and y and have a label
def scattP(xdata,ydata,label):
    sns.scatterplot(x=xdata, y=ydata,hue=label)
    pyplot.show()

#***FUNCTIONS TO USE ON SEVERAL COLUMNS IN DATA***    

#Make histogram of all numeric data in df
def histP_df(data):
    data.hist()#Perhaps a log transform or similar would be good?
    pyplot.show()

#Make boxplot histogram of all numeric data in df
def boxP_df(data,lrow=1,lcol=6):
    data.plot(kind='box', subplots=True, layout=(lrow,lcol), sharex=False, sharey=False)
    pyplot.show()

#Make scatte rmatrix of all numeric data in df
def scattP_df(data):
    scatter_matrix(data) 
    pyplot.show()    

