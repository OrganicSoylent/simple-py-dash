# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:33:01 2023

@author: Lutz
"""
from backend import get_current_value, get_historical_values, get_default_timerange
import frontend

if __name__ == '__main__':
    start_date, end_date = get_default_timerange()
    frontend.app.run_server(debug=True)
