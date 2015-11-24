#from pyspark import SparkContext, SparkConf 
#conf = SparkConf()
#sc   = SparkContext(conf = conf)
import sys
import seaborn
import glob
import os
import openpyxl


def ingest_iff_file(iff_file):
    records = {}
    with open(iff_file) as iff_file:
        iff_file.next() ### skip header
        for line in iff_file:
            print line.split()
            break

### Load in all files (currently just for 1 year)
iff_files = {}
tot_files = {}
dem_files = {}
cwd = os.getcwd()
for name in glob.glob(cwd + "/1999_*.csv"):
    if "IFF" in name:
        print name
        ingest_iff_file(name)




