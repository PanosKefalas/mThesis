import numpy as np
import pandas as pd

def accuracy(predicted, actual):
    
    predicted, actual = np.array(predicted), np.array(actual)
    mape = np.round(np.mean(np.abs((actual-predicted)/actual)), 3)
    #mape_r = np.round(mape, 3)
    corr = (np.corrcoef(predicted, actual)[0,1].round(3))**2
    #corr_r = np.round(corr, 3)
    
    return ({ 'mape':mape, 'corr':corr})

