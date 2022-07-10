# SPDX-License-Identifier: MIT
'''Main entry point for Hail Chaser'''
from radar import save_data, data_available
from kmz_extract import extract
from hail import hail

FILE_NAME = 'radar.zip'

save_data(FILE_NAME)
if data_available(FILE_NAME):
    data_frame = extract(FILE_NAME)
    hail(data_frame, 'Guadalajara, Mexico')
