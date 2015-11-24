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



import openpyxl
import sys



"""
with open(sys.argv[1]) as data:
    for record in data:
        print record.split('    ')
"""

