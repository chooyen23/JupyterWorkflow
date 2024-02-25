
import os
from urllib.request import urlretrieve
import pandas as pd
from sodapy import Socrata

FREMONT_URL = 'https://data.seattle.gov/resource/65db-xm6k.json'

def get_fremont_data(file_name='Fremont.csv',url=FREMONT_URL, force_download=False):
    
    '''Download and cache Fremont data
    
    Parameters
    ----------
    file_name:string (optional)
        location to save the data
    url: string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data
    
    Returns
    -------
     data : pandas.DataFrame
        The fremont bridge data   
    '''
    if force_download or not os.path.exists(file_name):
        # Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
        client = Socrata("data.seattle.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.seattle.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
        results = client.get("65db-xm6k", limit=3000)

# Convert to pandas DataFrame
        results_df = pd.DataFrame.from_records(results)
        results_df.to_csv('Fremont.csv')
    data = pd.read_csv('Fremont.csv',index_col='date', parse_dates=True)
    data.drop('Unnamed: 0', inplace=True, axis=1)
    return data