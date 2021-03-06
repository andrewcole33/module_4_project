from dateutil.relativedelta import relativedelta
import datetime
import pandas as pd

def future_dates(xlv_monthly_auto):
    '''
    Function: Adds future datetime entries to be filled later with predicted values 
    
    Input: Pandas DataFrame with datetime type index up to present day
    
    Output: Input DataFrame with future DateTime index entries to be filled later on.
    
    '''
    start_auto = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
    date_list_auto = [start_auto + relativedelta(months=x) for x in range(0,12)]
    future_auto = pd.DataFrame(index = date_list_auto, columns = xlv_monthly_auto.columns)
    xlv_monthly_auto = pd.concat([xlv_monthly_auto, future_auto])
    
    return xlv_monthly_auto