"""
The Healthy Eating Index (HEI) is a measure of diet quality that assesses conformance to federal dietary guidance. USDA calculated Healthy Eating Index component and overall scores from dietary recall interviews collected during the National Health and Nutrition Examination Survey (NHANES).

The overall HEI score is the sum of 10 dietary components, weighted equally. Each component of the index has a maximum score of 10 and a minimum score of zero. The maximum overall HEI score is 100. High component scores indicate intakes close to the recommended ranges or amounts; low component scores indicate less compliance with the recommended ranges or amounts.

Adequacy Components:
- Total Fruit 
- Whole Fruit
- Total Vegetables
- Greens and Beans
- Whole Grains
- Dairy
- Total Protein Foods
- Seafood and Plant Proteins
- Fatty Acids

Moderation Components: 
- Refined Grains
- Sodium
- Empty Calories 

"""


def hei_score(dietary_recall):
    ### Dictionary whose keys are HEI adequacy components,
    ### values are [MaxPoints, Unit Used, Standard for Max, Standard for Min]
    ### Fatty Acid adequacy is scored separately.
    adequacy_guidelines = {"Total Fruit": [5, 'cup', 0.8, 0],
                           "Whole Fruit": [5, 'cup', 0.4, 0],
                           "Total Vegetables": [5, 'cup', 1.1, 0],
                           "Greens and Beans": [5, 'cup', 0.2, 0],
                           "Whole Grains": [10, 'oz', 1.5, 0],
                           "Dairy": [10, 'cup', 1.3, 0],
                           "Total Protein": [5, 'oz', 2.5, 0],
                           "Seafood and Plant Protein": [5, 'oz', 0.8, 0]}
    
    moderation_guidelines = {"Refined Grains": [10, 'oz', 1.8, 4.3],
                             "Sodium": [10, 'gram', .1, 2.0],
                             "Empty Calories": [20, 'percent energy', 19, 50]}

    adequacy_score = 0
    fatty_acid_adeqacy_score = 0
    moderation_score = 0


    total_score = 0
    return total_score         


class Respondent(object):
    def __init__(self, sequence_number, year):
        self.sn = sequence_number
        self.yr = year
        self.iff_records = []
        self.tot_record = []
        self.dem_record = []
        self.dem_data = {'age': 0, 'sex': 0, 'edu': 0, 'income': 0}
        self.hei = 0
    
    def extract_food_codes(self):
        food_codes = []
        for r in self.iff_records:
            food_codes.append(int(r[15]))
        return food_codes

    def compute_hei(self):

        ### Compute adequacy components
        food_codes = self.extract_food_codes()
        ### Categorize 

        ### Compute fatty acid component
        pufas = float(self.tot_record[18])
        mufas = float(self.tot_record[17])
        sfas  = float(self.tot_record[16])
        fatty_acid_score = (pufas + mufas) / sfas
        fatty_acid_points = min((fatty_acid_score - 1.2) * (10/(2.5 - 1.2)), 10)
            
        ### Compute moderation components


        print pufas
        print mufas
        print sfas
        print fatty_acid_score
        print fatty_acid_points
        print food_codes

    

import sys

respondents = {}


"""
Do a pass through the individual foods file
"""
with open(sys.argv[1]) as iff_data:
    year = 1999
    iff_headers = iff_data.next().split(',')
    #print len(iff_headers)
    for line in iff_data:
        record = line.split(',') 
        sequence_number = int(record[0])
        
        #print record
        #print len(record)

        ### If this is the first time encountering the current sequence number,
        ### create a new respondent object. If the sequence number has been seen
        ### before, accumulate relevant data into existing respondent object
        if sequence_number not in respondents:
            ### Create Respondent instance
            r = Respondent(sequence_number, year)
            ### Add current line to r's list of raw iff records
            r.iff_records.append(record)
            ### Insert Respondent instance into dict of all respondents under
            ### its sequence number
            respondents[sequence_number] = r 
        else:
            ### Add current line to r's list of raw records
            respondents[sequence_number].iff_records.append(record)


"""
Now do a pass through the dietary totals file 
WARNING: There are sequence numbers in here that AREN'T in the IFF file...
"""
with open(sys.argv[2]) as tot_data:
    tot_headers = tot_data.next().split(',')
    for line in tot_data:
        record = line.split(',')
        sequence_number = int(record[0])
        if sequence_number in respondents:
            respondents[sequence_number].tot_record = record


"""
Now do a pass through the demographic data file
"""
with open(sys.argv[3]) as dem_data:
    dem_headers = dem_data.next().split(',')
    for line in dem_data:
        record = line.split(',')
        sequence_number = int(record[0])
        if sequence_number in respondents:
            respondents[sequence_number].dem_record = record


        
print respondents[1].sn
print respondents[1].yr
#print respondents[1].iff_records
print respondents[1].dem_data
#print respondents[1].extract_food_codes()

print "DRXTOT DATA"
print respondents[1].tot_record

print "DEMO DATA"
print respondents[1].dem_record
         
        
print "FOOD CODES / HEI STUFF"
respondents[1].compute_hei()






