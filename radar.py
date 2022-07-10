# SPDX-License-Identifier: MIT
'''Script to download KMZ radar file.'''

from os.path import exists
from datetime import datetime, timezone
import requests

BASE_PATH = 'http://iam.cucei.udg.mx/radar/iam'
API = BASE_PATH + '/api/api_radar.php?tipo_solicitud=kmz_act'
HEADERS = {'content-type': 'application/x-www-form-urlencoded'}

def save_data(file_name):
    '''Get current radar data as KMZ file.'''
    utc_now = datetime.now(timezone.utc)
    date = utc_now.strftime("%Y%m%d")
    data = 'radar=_ZH_&fecha=' + date

    print('Getting KMZ file for', utc_now)
    response = requests.post(API, headers=HEADERS, data=data)
    kmz = BASE_PATH + response.text[2:]

    response = requests.get(kmz)
    with open(file_name, 'wb') as file:
        file.write(response.content)

def data_available(file_name):
    '''Check if data file exists'''
    return exists(file_name)
