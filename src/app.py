#from pyspark import SparkContext, SparkConf 
#conf = SparkConf()
#sc   = SparkContext(conf = conf)
import sys
import seaborn
import glob
import os
import openpyxl

"""
nut_data = {iff: , tot: }
dem_data = {age: , sex: , income: , edu: }
"""
def respondent(object):
    def __init__(self, sequence_num, year):
        self.sn = sequence_num
        self.yr = year
        self.hei_scores = {}
        self.nut_data = {}
        self.dem_data = {}

    def assign_hei_score(self):

    def populate_dem_data(self):

    def populate_nut_data(self):
        


def ingest_iff_file(iff_file):
    records = {}
    with open(iff_file) as iff_file:
        iff_file.next() ### skip header
        for line in iff_file:
            print line.split()
            break

def ingest_tot_file(tot_file):



def ingest_dem_file(dem_file):



### Load in all files (currently just for 1 year)
iff_files = {}
tot_files = {}
dem_files = {}
cwd = os.getcwd()
for name in glob.glob(cwd + "/1999_*.csv"):
    if "IFF" in name:
        print name
        ingest_iff_file(name)




