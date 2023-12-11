# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:02:59 2023

@author: jacob
"""

import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

DATA = pd.read_excel(r'INSERT FILEPATH WITH SELECTED GEOGRAPHY"S DATA HERE')
CENTROIDS = pd.read_excel(r'INSERT FILEPATH WITH SELECTED GEOGRAPHY"S CENTROIDS HERE')

CENTROIDS = CENTROIDS.merge(DATA, how = 'inner')

centroids = np.empty((CENTROIDS.shape[0],2))
centroids[:,0] = CENTROIDS['LON']
centroids[:,1] = CENTROIDS['LAT']

race = np.empty((DATA.shape[0],10))

race[:,0] = DATA['B02001_001E']
race[:,1] = DATA['B02001_002E']
race[:,2] = DATA['B02001_003E']
race[:,3] = DATA['B02001_004E']
race[:,4] = DATA['B02001_005E']
race[:,5] = DATA['B02001_006E']
race[:,6] = DATA['B02001_007E']
race[:,7] = DATA['B02001_008E']
race[:,8] = DATA['B02001_009E']
race[:,9] = DATA['B02001_010E']

income = np.empty((DATA.shape[0],1))

income[:,0] = DATA['B19013_001E']

transplant = np.empty((DATA.shape[0],3))

transplant[:,0] = DATA['B05002_001E']
transplant[:,1] = DATA['B05002_004E']
transplant[:,2] = DATA['B05002_009E']

immigrant = np.empty((DATA.shape[0],2))

immigrant[:,0] = DATA['B05002_001E']
immigrant[:,1] = DATA['B05002_013E']

home_cost = np.empty((DATA.shape[0],1))

home_cost[:,0] = DATA['B25077_001E']

rent = np.empty((DATA.shape[0],1))

rent[:,0] = DATA['B25064_001E']

dependency = np.empty((DATA.shape[0],19))

dependency[:,0] = DATA['B01001_001E']
dependency[:,1] = DATA['B01001_003E']
dependency[:,2] = DATA['B01001_004E']
dependency[:,3] = DATA['B01001_005E']
dependency[:,4] = DATA['B01001_020E']
dependency[:,5] = DATA['B01001_021E']
dependency[:,6] = DATA['B01001_022E']
dependency[:,7] = DATA['B01001_023E']
dependency[:,8] = DATA['B01001_024E']
dependency[:,9] = DATA['B01001_025E']
dependency[:,10] = DATA['B01001_027E']
dependency[:,11] = DATA['B01001_028E']
dependency[:,12] = DATA['B01001_029E']
dependency[:,13] = DATA['B01001_044E']
dependency[:,14] = DATA['B01001_045E']
dependency[:,15] = DATA['B01001_046E']
dependency[:,16] = DATA['B01001_047E']
dependency[:,17] = DATA['B01001_048E']
dependency[:,18] = DATA['B01001_049E']

population = np.empty((DATA.shape[0],1))

population[:,0] = DATA['B01003_001E']

def RACE (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    O_W = O[:,1]/O[:,0] #Origin White 
    D_W = D[:,1]/D[:,0] #Destination White    
    
    W = abs(O_W - D_W)
    
    O_B = O[:,2]/O[:,0] #Origin Black
    D_B = D[:,2]/D[:,0] #Destination Black    
    
    B = abs(O_B - D_B)
    
    O_NA = O[:,3]/O[:,0] #Origin Native American
    D_NA = D[:,3]/D[:,0] #Destination Native American    
    
    NA = abs(O_NA - D_NA)
    
    O_A = O[:,4]/O[:,0] #Origin Asian
    D_A = D[:,4]/D[:,0]#Destination Asian    
    
    A = abs(O_A - D_A)
    
    O_NH = O[:,5]/O[:,0] #Origin Native Hawaiian
    D_NH = D[:,5]/D[:,0] #Destination Hawaiian    
    
    NH = abs(O_NH - D_NH)
    
    O_SO = O[:,6]/O[:,0] #Origin Some Other Race
    D_SO = D[:,6]/D[:,0] #Destination Some Other Race    
    
    SO = abs(O_SO - D_SO)
    
    O_TW = O[:,7]/O[:,0] #Origin Two or More Races
    D_TW = D[:,7]/D[:,0] #Destination Two or More Races    
    
    TW = abs(O_TW - D_TW)
    
    O_TW1 = O[:,8]/O[:,0] #Origin Two or More Races Excluding Some Other Race
    D_TW1 = D[:,8]/D[:,0] #Destination Two or More Races Excluding Some Other Race    
    
    TW1 = abs(O_TW1 - D_TW1)
    
    O_TW2 = O[:,9]/O[:,0] #Origin Two or More Races Excluding Some Other Race and Three or More Races
    D_TW2 = D[:,9]/D[:,0] #Destination Two or More Races Excluding Some Other Race and Three or More Races
    
    TW2 = abs(O_TW2 - D_TW2)
    
    RACE_SCORE = W + B + NA + A + NH + SO + TW + TW1 + TW2
    
    return(RACE_SCORE)

def INCOME (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    INCOME_SCORE = D[:,0]/O[:,0]
    
    return(INCOME_SCORE)

def TRANSPLANT (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    O_TR_BI = O[:,1]/O[:,0] #Born in US
    O_TR_BO = O[:,2]/O[:,0] #Born outiside US
    
    D_TR_BI = D[:,1]/D[:,0] #Born in US
    D_TR_BO = D[:,2]/D[:,0] #Born outiside US
    
    TR_BI = abs(O_TR_BI - D_TR_BI)
    TR_BO = abs(O_TR_BO - D_TR_BO)
    
    TRANSPLANT_SCORE = TR_BI + TR_BO
    
    return(TRANSPLANT_SCORE)

def IMMIGRANT (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    O_IM = O[:,1]/O[:,0] #Born in US
    
    D_IM = D[:,1]/D[:,0] #Born in US
    
    IMMIGRANT_SCORE = abs(O_IM - D_IM)
    
    return(IMMIGRANT_SCORE)

def HOME_COST (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    HOME_COST_SCORE = D[:,0]/O[:,0]
    
    return(HOME_COST_SCORE)

def RENT (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    RENT_SCORE = D[:,0]/O[:,0]
   
    return(RENT_SCORE)

def DEPENDENCY (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    O_D = (O[:,1] 
           + 
           O[:,2] 
           + 
           O[:,3] 
           + 
           O[:,4] 
           + 
           O[:,5] 
           +
           O[:,6] 
           + 
           O[:,7] 
           + 
           O[:,8] 
           + 
           O[:,9]
           +
           O[:,10] 
           + 
           O[:,11] 
           + 
           O[:,12] 
           + 
           O[:,13] 
           + 
           O[:,14] 
           + 
           O[:,15] 
           + 
           O[:,16] 
           + 
           O[:,17] 
           + 
           O[:,18])
    
    O_ND = O[:,0] - O_D
    O_DR = O_D/O_ND
    
    D_D =(D[:,1] 
           + 
           D[:,2] 
           + 
           D[:,3] 
           + 
           D[:,4] 
           + 
           D[:,5] 
           +
           D[:,6] 
           + 
           D[:,7] 
           + 
           D[:,8] 
           + 
           D[:,9]
           +
           D[:,10] 
           + 
           D[:,11] 
           + 
           D[:,12] 
           + 
           D[:,13] 
           + 
           D[:,14] 
           + 
           D[:,15] 
           + 
           D[:,16] 
           + 
           D[:,17] 
           + 
           D[:,18])
    
    D_ND = D[:,0] - D_D
    D_DR = D_D/D_ND
    
    DEPENDENCY_SCORE = abs(O_DR - D_DR)
   
    return(DEPENDENCY_SCORE)

#From: Michael Dunn | http://evoling.net/code/haversine/
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    
    distance = c * r
    return(distance)

def POPULATION (origin_array, destination_array):
    O = origin_array
    D = destination_array
    
    POPULATION_SCORE = D[:,0]/O[:,0]
    
    return(POPULATION_SCORE)
    

calibration = pd.read_excel(r'INSERT FILEPATH FOR VARIABLE COEFFICIENTS HERE')
race_cal = calibration['MEAN'][0]
income_cal = calibration['MEAN'][1]
transplant_cal = calibration['MEAN'][2]
immigrant_cal = calibration['MEAN'][3]
home_cost_cal = calibration['MEAN'][4]
rent_cal = calibration['MEAN'][5]
dependency_cal = calibration['MEAN'][6]
distance_cal = calibration['MEAN'][7]
population_cal = calibration['MEAN'][8]

attraction = np.empty((DATA.shape[0],DATA.shape[0]))


for i in range(DATA.shape[0]):
    scores = np.empty(((DATA.shape[0]),9))
    
    var = race
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,0] = RACE(O, D)
    
    var = income
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,1] = INCOME(O, D)
    
    var = transplant
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,2] = TRANSPLANT(O, D)
    
    var = immigrant
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,3] = IMMIGRANT(O, D)
    
    var = home_cost
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,4] = HOME_COST(O, D)
    
    var = rent
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,5] = RENT(O, D)
    
    var = dependency
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,6] = DEPENDENCY(O, D)
    
    var = centroids
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    
    for j in range(DATA.shape[0]):
    
        scores[j,7] = haversine(O[0,0], O[0,1], D[j,0], D[j,1]) 
    
    var = population
    O = var[i,:]
    O = var[i,:].reshape(1,var.shape[1])
    D = var
    scores[:,8] = POPULATION(O, D)
    
    attraction[:,i] = ((scores[:,0] * race_cal)
                      +
                      (scores[:,1] * income_cal)
                      +
                      (scores[:,2] * transplant_cal)
                      +
                      (scores[:,3] * immigrant_cal)
                      +
                      (scores[:,4] * home_cost_cal)
                      +
                      (scores[:,5] * rent_cal)
                      +
                      (scores[:,6] * dependency_cal)
                      +
                      (scores[:,7] * distance_cal)
                      +
                      (scores[:,8] * population_cal))
    

    

attraction_df = pd.DataFrame(attraction)
attraction_df.to_excel(r'INSERT FINAL SAVEPATH FOR ATTRACTION TABLE HERE')
