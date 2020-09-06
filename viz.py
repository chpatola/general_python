import seaborn as sns
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
from statsmodels.nonparametric.smoothers_lowess import lowess
from matplotlib import rcParams
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.nonparametric.smoothers_lowess import lowess
import numpy as np
import scipy.stats as stats
import pandas as pd

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

# Make Residuals vs fitted plot
def res_fitP(linmodel):
    residuals =linmodel.resid
    fitted = linmodel.fittedvalues
    smoothed = lowess(residuals,fitted)
    top3 = abs(residuals).sort_values(ascending = False)[:3]

    pyplot.rcParams.update({'font.size': 16})
    pyplot.rcParams["figure.figsize"] = (8,7)
    fig, ax = pyplot.subplots()
    ax.scatter(fitted, residuals, edgecolors = 'k', facecolors = 'none')
    ax.plot(smoothed[:,0],smoothed[:,1],color = 'r')
    ax.set_ylabel('Residuals')
    ax.set_xlabel('Fitted Values')
    ax.set_title('Residuals vs. Fitted')
    ax.plot([min(fitted),max(fitted)],[0,0],color = 'k',linestyle = ':', alpha = .3)

    for i in top3.index:
        ax.annotate(i,xy=(fitted[i],residuals[i]))

    pyplot.show()

# Make Normal Q - Q plot
def q_qP(linmodel):
    sorted_student_residuals = pd.Series(linmodel.get_influence().resid_studentized_internal)
    sorted_student_residuals.index = linmodel.resid.index
    sorted_student_residuals = sorted_student_residuals.sort_values(ascending = True)
    df = pd.DataFrame(sorted_student_residuals)
    df.columns = ['sorted_student_residuals']
    df['theoretical_quantiles'] = stats.probplot(df['sorted_student_residuals'], dist = 'norm', fit = False)[0]
    rankings = abs(df['sorted_student_residuals']).sort_values(ascending = False)
    top3 = rankings[:3]

    fig, ax = pyplot.subplots()
    x = df['theoretical_quantiles']
    y = df['sorted_student_residuals']
    ax.scatter(x,y, edgecolor = 'k',facecolor = 'none')
    ax.set_title('Normal Q-Q')
    ax.set_ylabel('Standardized Residuals')
    ax.set_xlabel('Theoretical Quantiles')
    ax.plot([np.min([x,y]),np.max([x,y])],[np.min([x,y]),np.max([x,y])], color = 'r', ls = '--')
    for val in top3.index:
        ax.annotate(val,xy=(df['theoretical_quantiles'].loc[val],df['sorted_student_residuals'].loc[val]))
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

