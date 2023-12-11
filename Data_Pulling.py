# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:13:09 2023

@author: jacob
"""

import pandas as pd
import aiohttp
import asyncio
import math
import nest_asyncio
import numpy as np


df = pd.read_excel(r'INSERT EXCEL SHEET WITH VARIABLES HERE')

geo = pd.read_excel(r'INSERT EXCEL SHEET WITH SELECTED GEOGRAPHY HERE')


geo = geo[geo['y2_statefips'] < 57]

variables = df
selected_geography = geo

variables_list = list(variables['Variable'])
state_list = list(selected_geography['y2_statefips'])
state_list = state_list[:]
county_list = list(selected_geography['y2_countyfips'])
county_list = county_list[:]


url = 'https://api.census.gov/data'
year = 'INSERT SELECTED YEAR HERE'
dataset = 'acs'
sub_dataset = 'acs1'
key = 'INSERT CENSUS API KEY HERE'

base_request = f'{url}/{year}/{dataset}/{sub_dataset}'

pre_processed_tasks = []

variable_range = 30


for i in range(math.ceil((len(variables))/variable_range)):

    
    if ((len(variables) - (i*variable_range)) >= variable_range):
        variables_subset = variables_list[(i*variable_range):((i*variable_range) + variable_range)]
        variables_subset = ','.join(variables_subset)
    else:
        variables_subset = variables_list[(i*variable_range):len(variables)]
        variables_subset = ','.join(variables_subset)
         

    for j in range(len(selected_geography)):
        state = str(state_list[j])
        state = state.rjust(2,'0')
        county = str(county_list[j])
        county = county.rjust(3,'0')
        request = f'{base_request}?get=NAME,{variables_subset}&for=county:{county}&in=state:{state}&key={key}'
        pre_processed_tasks.append(request)
        

nest_asyncio.apply() #Allows code below to run

async def get_results(session, request):
    async with session.get(request) as resp:
        results = await resp.json(content_type=None)
    
        return (results)

async def main(base_request):
    async with aiohttp.ClientSession() as session:

        tasks = []
        
        for i in range(len(pre_processed_tasks)):
            request = pre_processed_tasks[i]
            tasks.append(asyncio.ensure_future(get_results(session, request)))

        acs_results = await asyncio.gather(*tasks)
        
        return (acs_results)

acs_results = asyncio.run(main(base_request))

acs_results_no_nonetype = []

for i in range(len(acs_results)):
    if acs_results[i] != None:
         acs_results_no_nonetype.append(acs_results[i])
    

results_comprehension = np.empty((len(acs_results_no_nonetype),len(acs_results_no_nonetype[0][0])))
results_comprehension = results_comprehension.astype(str)

results = np.empty((len(acs_results_no_nonetype),len(acs_results_no_nonetype[0][0])))
results = results.astype(str)

for i in range(len(acs_results_no_nonetype)):
    for j in range(len(acs_results_no_nonetype[i][0])):
        results_comprehension[i][j] = acs_results_no_nonetype[i][0][j]
        results[i][j] = acs_results_no_nonetype[i][1][j]
     
results_comprehension = results_comprehension[:,1:]
results_df = pd.DataFrame(results)

consolidated_results = pd.DataFrame(np.empty((len(results_df[0].drop_duplicates()),len(variables_list))))

consolidated_results = consolidated_results.reindex(variables_list, axis = 1)


for i in range(results.shape[0]):
    for j in range(results_comprehension.shape[1]):
        geography = str(results[i,0])
        variable = str(results_comprehension[i,j])
        
        consolidated_results.loc[geography, variable] =  results[i,j+1]


consolidated_results.to_excel(r'INSERT YOUR SAVE PATH HERE')
