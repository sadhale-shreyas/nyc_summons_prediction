# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:32:35 2023

@author: swath
"""
def count_boroughs(data):
    borough_counts = data['boro'].value_counts().sort_index()
    return borough_counts

import matplotlib.pyplot as plt

def plot_age_group_distribution(nyc_summon):
    plt.figure(figsize=(10, 6))
    plt.hist(nyc_summon['age_group'], edgecolor='black', bins=14, color='salmon')
    plt.xlabel('Age Group')
    plt.ylabel('Frequency')
    plt.title('Age Group Distribution')
    plt.show()
    
    
def plot_race_distribution(data):
    race_counts = data['race'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(race_counts.values, labels=race_counts.index, autopct='%1.1f%%')
    plt.title('Distribution of Race')
