# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:26:13 2017

@author: marinag
"""

def blend_garbanzo(chickpea_string):
    if 'hummus' in chickpea_string: 
        return chickpea_string
    else:
        return '{}_hummus'.format(chickpea_string)