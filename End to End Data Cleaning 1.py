import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import seaborn as sns

# calling / reading the data
df = pd.read_csv(r'C:\Users\USER\Desktop\ONECAMPUS PROJECT 2\Muskets_teamData_V2.csv')

df

df_copy = df.copy()

# Sub - task: 
#1. Extracting player names from player URL

Players = df_copy['playerUrl']
Players.head()


temp_list = []
for row in Players:
    vals = row.split('/')  # splitting the slashes in the url
    Player_name = vals[5]
    Player_name = (Player_name.replace('-', ' '))   # slitting the names and also splitting by under score
    temp_list.append( Player_name)
    
temp_list[:5]

df_copy['Player Name'] = temp_list

df_copy.columns

'''
2. Create a new column titled Player Status from the CONTRACT column with 3 labels ; 
a. 'Active' If the player has an active contract 
b. 'Free', if the player is free 
c. 'On Loan' if the player is on loan 
'''

df_copy.Contract.unique()

# exracting active, free and on loan from .unique
"""onLoandf = []
freedf = []
activedf = []

for row in df_copy.values:
    if 'On Loan' in row[10]:
        onLoandf.append(row)
    elif 'Free' in row[10]:
        freedf.append(row)
    else:
        activedf.append(row)"""
        

contract_list = []

for row in df_copy["Contract"]:
    if "On Loan" in row:
        contract_list.append("On Loan")
    elif "Free" in row:
        contract_list.append("Free")
    else:
        contract_list.append("Active")

df_copy["Player Status"] = contract_list

df_copy["Player Status"]

column = (list(df_copy.columns))
column[:11]

#df_copy[["Player Status", "Contract"]][df_copy["Player Status"] == "On Loan"].head()

'''
convert to integers 
4. Weight and Height, W/F, SM and IR Columns
'''

Weights = df_copy.Weight
Weights.unique()


kgWeights = []

# Replace NaN values with 0
Weights.fillna(0, inplace=True)

# In this next line of code, if slitting by number range was used, e.g [0:-2] or [0:-3] some values with not be completely \
# numerical while some values will be cut off e.g 56kg.
for weight in Weights.values:
    if isinstance(weight, str):
        if 'kg' in weight:
            kgWeights.append(int(weight.replace('kg', '')))  # replacing 'Kg' by a null
        elif 'lbs' in weight:
            lbs = int(weight.replace('lbs', ''))             # replacing "lbs" by a empty string
            kgWeights.append(int(round(lbs * 0.453592, 2)))  # converting lbs to kg and int
    elif isinstance(weight, (int)): 
            kgWeights.append(int(weight))
#print(kgWeights)
Weights = kgWeights
print(Weights)


df_copy.Weight = Weights
df_copy.Weight.head()

pd.concat([df_copy.Weight])

df_copy.Weight.unique()

Heights = df_copy.Height
Heights.unique() 

cmHeights = []

for height in Heights.values:
    if 'cm' in height:
        cmHeights.append(int(height.replace('cm', '')))
    elif '\'' in height:
        ft_in = height.split('\'')
        feet = int(ft_in[0])
        inches = int(ft_in[1].replace('"', ''))
        cmHeights.append(round((feet * 30.48) + (inches * 2.54))) # Due to the values in column Height, the values such '6\'4"' cm was coverted so it can be a real number
print(cmHeights)
Heights=cmHeights
print(Heights)

df_copy.Height = Heights
df_copy.Height.head()

pd.concat([df_copy.Height])

df_copy.Height.unique()

df_copy['SM'] = df_copy['SM'].replace('', 0)

valsList2 = []

for item in df_copy.SM.values:
    if isinstance(item, str):
        SMvals = (item.split(',')) # splitting by coma's
        SMnewVal = (int(item[0:-1])) # since the values of SM is appended with a star, the chopping off splitting method was used
    else:
        SMnewVal = '0'  # handle missing values as 0
    valsList2.append(int(SMnewVal))

print(valsList2[:5])


df_copy.SM = valsList2
df_copy.SM.head()

pd.concat([df_copy.SM])

df_copy.SM.unique()

df_copy['IR'] = df_copy['IR'].replace('', 0)

valsList3 = []

for item in df_copy.IR.values:
    if isinstance(item, str):
        IRvals = item.split('/')
        IRnewVal = (int(item[0:-1])) # since the values of IR is appended with a star, the chopping off splitting method was used
    else:
        IRnewVal = '0'  # handle missing values as 0
    valsList3.append(int(IRnewVal))

print(valsList3[:10])

df_copy.IR = valsList3
df_copy.IR.head()
pd.concat([df_copy.IR])

"""
import pandas as pd

# change the column names using rename()
df_copy = df_copy.rename(columns={'Release Clause': 'ReleaseClause', 'W/F': 'WF'})

# print the new column names
print(df_copy.columns)
"""

df_copy['W/F'].unique()

valsList4 = []

for item in df_copy['W/F'].values:  # Unlike IR & SM, W/F was putting in a string and list bracket because if ran it will return an error code
    if isinstance(item, str):
        WFvals = item.split('/')
        WFnewVal = (int(item[0:-1])) # since the values of W/F is appended with a star, the chopping off splitting method was used
    else:
        WFnewVal = '0'  # handle missing values as 0
    valsList4.append(int(WFnewVal))

print(valsList4[:10])


df_copy['W/F'] = valsList4
df_copy['W/F'].head()
pd.concat([df_copy['W/F']])

Values = df_copy.Value
Values.unique()

#5. Value, Wage and Release Clause columns: convert to Float

df_copy['Value'] = df_copy['Value'].replace('', 0) # replacing all null values with zero's

Values.values

cleanedValues = []
for val in Values.values:   
    if 'M' in val:
        cleanedValues.append(float(val.replace('€', '').replace('M', ''))*1000000)
    elif 'K' in val:
        cleanedValues.append(float(val.replace('€', '').replace('K', '')) * 1000)
    else:
        cleanedValues.append(0.0)


#print(cleanedValues)
Values=cleanedValues
print(Values)


df_copy.Value = Values
df_copy.Value.head()
pd.concat([df_copy.Value])

Wages = df_copy.Wage
Wages.unique()
df_copy['Wage'] = df_copy['Wage'].replace('', 0)  # replacing all null values with zero's


Wages.values

cleanedWages = []
for val in Wages.values:
    
    if 'M' in val:
        cleanedWages.append(float(val.replace('€', '').replace('M', ''))*1000000)
    elif 'K' in val:
        cleanedWages.append(float(val.replace('€', '').replace('K', ''))*1000)
    else:
        cleanedWages.append(0.0)

#print(cleanedValues)
Wages=cleanedWages
print(Wages)

df_copy.Wage = Wages
df_copy.Wage.head()

pd.concat([df_copy.Wage])

df_copy['Release Clause'].unique()


Release_list = []

R = df_copy["Release Clause"].copy()

# Replace NaN values with 0
R.fillna(0, inplace=True)

for row in R:
    
    if type(row) == int:
        Release_list.append(row)
#         print(row)
    else:
#         print(row[1:-1])
        if row[-1] == "M":
            Release_list.append(float(row[1:-1]) * 1000000) # mutiplying M by it respective figure in millions
            
        elif row[-1] == "K":
            Release_list.append(float(row[1:-1]) * 1000)   # mutiplying K by it respective figure in thousands
        else:
            Release_list.append(0)
            
# Dividind the abigous figures of M & K by there respective values
"""
for i in range(len(Release_list)):
    if Release_list[i] >= 1000000:
        Release_list[i] = Release_list[i] / 1000000
    elif Release_list[i] >= 1000:
        Release_list[i] = Release_list[i] / 1000
"""


Release_list
df_copy['Release Clause'] = Release_list
df_copy['Release Clause'].head()

pd.concat([df_copy['Release Clause']])

'''
3. Unpack the POSITIONS column into as many columns as there are positions and assign Boolean
values in the columns for each player as appropriate. Name the columns the play position 
'''

POSITIONS = df_copy.Positions.unique()
POSITIONS[:4]

# unpacking the values from .unique
pos_list = list(df_copy["Positions"].unique())
pos_list

pos_list = ", ".join(pos_list)
pos_list = pos_list.split(", ")

print(len(pos_list))

pos_list = list(set(pos_list))

print(len(pos_list))

pos_list

playerPos = []

for positions in df_copy.Positions.values:
    pos_listTable = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for p in pos_list:
        if p in positions:
            Pidx = pos_list.index(p)
            pos_listTable[Pidx] = 1
    playerPos.append(pos_listTable)        


playerPos

df_copyPos = pd.DataFrame(playerPos, columns = pos_list) # converting the postions list to a dataframe


df_copyPos

df_copy.Positions.values[0:5]

# merging the play positions table with the copy dataframe
df_copy = df_copy.join(df_copyPos) 

df_copy

df_copy.columns

# In positions, the positions of the players was unpacked and splitted by coma's.
# The unique values was gotten for the positions. A set fuction was used to remove the duplicates in the output
# The result was turned to a list for easy manipulation of the data.

# using playlist to add  boolean fuctons to positions on the dataframe
# To find alphabectic True and False using the (if,elif and else statement)
"""position = []

for i in df_copy.Positions:
    if i == 'LW':
        position.append("True")
    elif i == 'RW':
        position.append("True")
        
    elif i == 'CAM':
        position.append("True")
        
    elif i == 'LB':
        position.append("True")
        
    elif i == 'CDM':
        position.append("True")
        
    elif i == 'RWB':
        position.append("True")
    elif i == 'LWB':
        position.append("True")
    elif i == 'CM':
        position.append("True")
    elif i == 'LM':
        position.append("True")
    elif i == 'GK':
        position.append("True")
    elif i == 'RB':
        position.append("True")
    elif i == 'CF':
        position.append("True")
    elif i == 'RM':
        position.append("True")
    elif i == 'CB':
        position.append("True")
    elif i == 'ST':
        position.append("True")
    else:
        position.append("False")

position[:5]"""

# 6. Inspect the HITS column and ensure its float

HITS = df_copy.Hits
HITS.unique()


Hit_list = []
for row in HITS.values:
    if type(row) == int or type(row) == float:
        Hit_list.append(float(row))
    else:
        if row == 'K':
            Hit_list.append(float(0))
        elif row[-1] == 'K':
            if '.' in row:
                Hit_list.append(float(row[:-1]) * 1000)
            else:
                Hit_list.append(float(row[:-1]) / 1000)
        else:
            Hit_list.append(float(row))


Hit_list


df_copy.Hits = Hit_list
df_copy.Hits.head()


missing_hits = df_copy['Hits'].isnull().sum()

print(f"Missing values in 'Hits': {missing_hits}")


# In[68]:


df_copy['Hits'] = df_copy['Hits'].fillna(0)


# In[69]:


missing_hit = df_copy['Hits'].isnull().sum()

print(f"Missing values in 'Hits': {missing_hit}")


# In[ ]:





# In[70]:


''' Task 7:
    
    Create 5 new categorical columns for the Height, Weight, Release Clause, Value and Wage into
which you convert the respective values into clusters/labels as follows
a. Height: Bucket intervals of 10 years
b. Weight: Bucket intervals of 10 kg
c. Wage: bucket intervals of 50K
d. Value: bucket intervals of 50M
e. Release Clause: bucket intervals of 50M '''


# a. Height: Bucket intervals of 10 years

print(max(df_copy['Height']))
print(min(df_copy['Height']))

df_copy['binnedHeight'] = pd.cut(
df_copy['Height'], 
bins=6, 
labels=['150-160', '160-170', '170-180', '180-190', '190-200', '200-210'])


#b. Weight: Bucket intervals of 10 kg

print(max(df_copy['Weight']))
print(min(df_copy['Weight']))

df_copy['binnedWeight'] = pd.cut(
df_copy['Weight'], 
bins=6, 
labels=['50-60', '60-70', '70-80', '80-90', '90-100', '100-110'])

#c. Wage: bucket intervals of 50K

print(max(df_copy['Wage']))
print(min(df_copy['Wage']))

df_copy['binnedWage'] = pd.cut(
df_copy['Wage'], 
bins=11, 
labels=['50000-100000', '100000-150000', '150000-200000', '200000-250000', '250000-300000', '300000-350000', '350000-400000', '400000-450000', '450000-500000', '500000-550000', '550000-600000'])

#d. Value: bucket intervals of 50M

print(max(df_copy['Value']))
print(min(df_copy['Value']))

df_copy['binnedValue'] = pd.cut(
df_copy['Value'], 
bins=3, 
labels=['50000000-100000000', '100000000-150000000', '150000000-200000000'])


#e. Release Clause: bucket intervals of 50M

print(max(df_copy['Release Clause']))
print(min(df_copy['Release Clause']))

df_copy['binnedRelease Clause'] = pd.cut(
df_copy['Release Clause'], 
bins=4, 
labels=['50000000-100000000', '100000000-150000000', '150000000-200000000', '200000000-250000000'])

df_copy.columns


df_copy1 = df_copy.reindex(columns=['ID', 'Name', 'LongName', 'photoUrl', 'playerUrl', 'Nationality', 'Age',
       '↓OVA', 'POT', 'Club', 'Contract', 'Positions', 'Height', 'Weight',
       'Preferred Foot', 'BOV', 'Best Position', 'Joined', 'Loan Date End',
       'Value', 'Wage', 'Release Clause', 'Attacking', 'Crossing', 'Finishing',
       'Heading Accuracy', 'Short Passing', 'Volleys', 'Skill', 'Dribbling',
       'Curve', 'FK Accuracy', 'Long Passing', 'Ball Control', 'Movement',
       'Acceleration', 'Sprint Speed', 'Agility', 'Reactions', 'Balance',
       'Power', 'Shot Power', 'Jumping', 'Stamina', 'Strength', 'Long Shots',
       'Mentality', 'Aggression', 'Interceptions', 'Positioning', 'Vision',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'GK Reflexes', 'Total Stats',
       'Base Stats', 'W/F', 'SM', 'A/W', 'D/W', 'IR', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Player Name', 'Player Status','ST', 'CB',
       'CM', 'RW', 'LB', 'CF', 'CDM', 'GK', 'LWB', 'RM', 'RB', 'CAM', 'LM',
       'LW', 'RWB','binnedHeight','binnedWeight','binnedWage','binnedValue',
       'binnedRelease Clause','Hits'])  

df_copy1.head()

df_copy1.shape

df_copy1.info()

df_copy1.isna().sum()

# Treating for missing values
#using padding method to treat for missing values for ↓OVA
df_copy1['↓OVA'] .unique()

df_copy1['↓OVA']= df_copy1['↓OVA'].fillna(method = 'pad')

df_copy1['↓OVA'][:5]

df_copy1['POT'] .unique()

df_copy1['POT']= df_copy1['POT'].fillna(method = 'pad')


# Padding imputation is a method of imputing missing values in sequential data, such as time series or text data. It involves filling in missing values with a placeholder value, such as zero or a specific character, to make the length of each sequence uniform. This method was used because the values was sequencial values.
df_copy1['POT'][:5]


# This is a simple and fast method, but it can introduce bias if the missing values are not missing at random, and it can reduce the variability of the data. Therefore, the mean and median imputation method was used beacuse the values of the columns were missingf at reandoms.
df_copy1['Attacking'].fillna(df_copy1['Attacking'].mean(), inplace = True)
df_copy1['Attacking'][:5]

df_copy1['Crossing'].fillna(df_copy1['Crossing'].median(), inplace = True)
df_copy1['Crossing'][:5]


df_copy1['Finishing'].fillna(df_copy1['Finishing'].median(), inplace = True)
df_copy1['Finishing'][:5]


df_copy1['Heading Accuracy'] .unique()
df_copy1['Heading Accuracy'].fillna(df_copy1['Heading Accuracy'].median(), inplace = True)
df_copy1['Heading Accuracy'][:5]



df_copy1['Short Passing'] .unique()
# Replace underscores with empty strings
df_copy1['Short Passing'] = [float(s.replace('_', '')) if isinstance(s, str) else s for s in df_copy1['Short Passing']]
df_copy1['Short Passing'].unique()
df_copy1['Short Passing'].fillna(df_copy1['Short Passing'].median(), inplace = True)
df_copy1['Short Passing'][:5]

df_copy1['Volleys'].unique()
df_copy1['Volleys'].fillna(df_copy1['Volleys'].median(), inplace = True)
df_copy1['Volleys'][:5]

df_copy1['Skill'].unique()
df_copy1['Skill'].fillna(df_copy1['Skill'].mean(), inplace = True)
df_copy1['Skill'][:5]


df_copy1['Dribbling'].unique()

# Replace underscores with empty strings
df_copy1['Dribbling'] = [float(s.replace('_', '')) if isinstance(s, str) else s for s in df_copy1['Dribbling']]
df_copy1['Dribbling'].fillna(df_copy1['Dribbling'].mean(), inplace = True)
df_copy1['Dribbling'] .unique()


df_copy1['Curve'][:5]
df_copy1['Curve'].fillna(df_copy1['Curve'].mean(), inplace = True)
df_copy1['Curve'] .unique()

df_copy1['FK Accuracy'].unique()
df_copy1['FK Accuracy'].fillna(df_copy1['FK Accuracy'].mean(), inplace = True)
df_copy1['FK Accuracy'][:5]

df_copy1['Long Passing'].unique()
df_copy1['Long Passing'].fillna(df_copy1['Long Passing'].mean(), inplace = True)
df_copy1['Long Passing'][:5]

df_copy1['Ball Control'].unique()
df_copy1['Ball Control'].fillna(df_copy1['Ball Control'].mean(), inplace = True)
df_copy1['Ball Control'][:5]

df_copy1['Movement'].unique()
df_copy1['Movement'].fillna(df_copy1['Movement'].mean(), inplace = True)
df_copy1['Movement'][:5]

df_copy1['Acceleration'].unique()
df_copy1['Acceleration'].fillna(df_copy1['Acceleration'].mean(), inplace = True)
df_copy1['Acceleration'][:5]


df_copy1['Sprint Speed'].unique()
df_copy1['Sprint Speed'].fillna(df_copy1['Sprint Speed'].mean(), inplace = True)
df_copy1['Sprint Speed'][:5]

df_copy1['Agility'].unique()
df_copy1['Agility'].fillna(df_copy1['Agility'].mean(), inplace = True)
df_copy1['Agility'][:5]


df_copy1['Reactions'].unique()
df_copy1['Reactions'].fillna(df_copy1['Reactions'].mean(), inplace = True)
df_copy1['Reactions'][:5]


df_copy1['Balance'].unique()
df_copy1['Balance'].fillna(df_copy1['Balance'].mean(), inplace = True)
df_copy1['Balance'][:5]


df_copy1['Power'].unique()
df_copy1['Power'].fillna(df_copy1['Power'].mean(), inplace = True)
df_copy1['Power'][:5]


df_copy1['Shot Power'].unique()
df_copy1['Shot Power'].fillna(df_copy1['Shot Power'].mean(), inplace = True)
df_copy1['Shot Power'][:5]


df_copy1['Jumping'].unique()
df_copy1['Jumping'].fillna(df_copy1['Jumping'].mean(), inplace = True)
df_copy1['Jumping'][:5]

df_copy1['Stamina'].unique()
df_copy1['Stamina'].fillna(df_copy1['Stamina'].mean(), inplace = True)
df_copy1['Stamina'][:5]

df_copy1['Strength'].unique()
df_copy1['Strength'].fillna(df_copy1['Strength'].mean(), inplace = True)
df_copy1['Strength'][:5]


df_copy1['Long Shots'].unique()
df_copy1['Long Shots'].fillna(df_copy1['Long Shots'].mean(), inplace = True)
df_copy1['Long Shots'][:5]

df_copy1['Mentality'].unique()
df_copy1['Mentality'].fillna(df_copy1['Mentality'].mean(), inplace = True)
df_copy1['Mentality'][:5]

df_copy1['Aggression'].unique()
df_copy1['Aggression'].fillna(df_copy1['Aggression'].mean(), inplace = True)
df_copy1['Aggression'][:5]


df_copy1['Interceptions'].unique()
df_copy1['Interceptions'].fillna(df_copy1['Interceptions'].mean(), inplace = True)
df_copy1['Interceptions'][:5]


df_copy1['Positioning'].unique()
df_copy1['Positioning'].fillna(df_copy1['Positioning'].mean(), inplace = True)
df_copy1['Positioning'][:5]

df_copy1['Penalties'].unique()
df_copy1['Penalties'].fillna(df_copy1['Penalties'].mean(), inplace = True)
df_copy1['Penalties'][:5]


df_copy1['Composure'].unique()
df_copy1['Composure'].fillna(df_copy1['Composure'].mean(), inplace = True)
df_copy1['Composure'][:5]


df_copy1['Defending'].unique()
df_copy1['Defending'].fillna(df_copy1['Defending'].mean(), inplace = True)
df_copy1['Defending'][:5]

df_copy1['Marking'].unique()
df_copy1['Marking'].fillna(df_copy1['Marking'].mean(), inplace = True)
df_copy1['Marking'][:5]


df_copy1['Standing Tackle'].unique()
df_copy1['Standing Tackle'].fillna(df_copy1['Standing Tackle'].mean(), inplace = True)
df_copy1['Standing Tackle'][:5]

df_copy1['Sliding Tackle'].unique()
df_copy1['Sliding Tackle'].fillna(df_copy1['Sliding Tackle'].mean(), inplace = True)
df_copy1['Sliding Tackle'][:5]

df_copy1['Goalkeeping'].unique()
df_copy1['Goalkeeping'].fillna(df_copy1['Goalkeeping'].mean(), inplace = True)
df_copy1['Goalkeeping'][:5]

df_copy1['GK Diving'].unique()
df_copy1['GK Diving'].fillna(df_copy1['GK Diving'].mean(), inplace = True)
df_copy1['GK Diving'][:5]

df_copy1['GK Handling'].unique()
df_copy1['GK Handling'].fillna(df_copy1['GK Handling'].mean(), inplace = True)
df_copy1['GK Handling'][:5]

df_copy1['GK Kicking'].unique()

df_copy1['GK Kicking'].fillna(df_copy1['GK Kicking'].mean(), inplace = True)
df_copy1['GK Kicking'][:5]

df_copy1['GK Positioning'].unique()

df_copy1['GK Positioning'].fillna(df_copy1['GK Positioning'].mean(), inplace = True)
df_copy1['GK Positioning'][:5]

df_copy1['GK Reflexes'].unique()

df_copy1['GK Reflexes'].fillna(df_copy1['GK Reflexes'].mean(), inplace = True)
df_copy1['GK Reflexes'][:5]

df_copy1['Total Stats'].unique()
df_copy1['Total Stats'].fillna(df_copy1['Total Stats'].mean(), inplace = True)
df_copy1['Total Stats'][:5]

df_copy1['D/W'].unique()

# Fill missing values with mode
mode_value = df_copy1['D/W'].mode()[0]
df_copy1['D/W'].fillna(mode_value, inplace=True)
df_copy1['D/W'][:5]
df_copy1['PAC'].unique()

df_copy1['PAC'].fillna(df_copy1['PAC'].mean(), inplace = True)
df_copy1['PAC'][:5]

df_copy1['SHO'].unique()

df_copy1['SHO'].fillna(df_copy1['SHO'].mean(), inplace = True)
df_copy1['SHO'][:5]

df_copy1['PAS'].unique()

df_copy1['PAS'].fillna(df_copy1['PAS'].mean(), inplace = True)
df_copy1['PAS'][:5]

df_copy1['DRI'].unique()

df_copy1['DRI'].fillna(df_copy1['DRI'].mean(), inplace = True)
df_copy1['DRI'][:5]

df_copy1['DEF'].unique()


df_copy1['DEF'].fillna(df_copy1['DEF'].mean(), inplace = True)
df_copy1['DEF'][:5]

df_copy1['PHY'].unique()

df_copy1['PHY'].fillna(df_copy1['PHY'].mean(), inplace = True)
df_copy1['PHY'][:5]

# Treating for Loan Date End 
df_copy1['Loan Date End'].unique()

# The data contains a lot of missing data in thousands. Dropping to keep and re-introducing it back when predicting using Hits
df_copy2 = df_copy1.drop('Loan Date End', axis = 1)
df_copy2.isna().sum()
df_copy2.info(verbose=True, show_counts=True)

#Dropping Irrelevant Columns

list(df_copy2.columns)


refcols = [
 'Age',
 '↓OVA',
 'POT',
 'BOV',
 'Best Position',
 'Attacking',
 'Crossing',
 'Finishing',
 'Heading Accuracy',
 'Volleys',
 'Skill',
 'Curve',
 'FK Accuracy',
 'Long Passing',
 'Ball Control',
 'Movement',
 'Acceleration',
 'Sprint Speed',
 'Agility',
 'Reactions',
 'Balance',
 'Power',
 'Shot Power',
 'Jumping',
 'Stamina',
 'Strength',
 'Long Shots',
 'Mentality',
 'Aggression',
 'Interceptions',
 'Positioning',
 'Vision',
 'Penalties',
 'Composure',
 'Defending',
 'Marking',
 'Standing Tackle',
 'Sliding Tackle',
 'Goalkeeping',
 'GK Diving',
 'GK Handling',
 'GK Kicking',
 'GK Positioning',
 'GK Reflexes',
 'Total Stats',
 'Base Stats',
 'A/W',
 'D/W',
 'PAC',
 'SHO',
 'PAS',
 'DRI',
 'DEF',
 'PHY',
 'Player Status',
 'LM',
 'CDM',
 'CM',
 'LWB',
 'RW',
 'LB',
 'RWB',
 'RB',
 'GK',
 'RM',
 'CB',
 'ST',
 'CAM',
 'LW',
 'CF',
 'Weight',
 'Height',
 'Value',
 'Wage',
 'Release Clause',
 'Dribbling',
 'Short Passing',
 'W/F',
 'SM',
 'IR',
 'binnedHeight',
 'binnedWeight',
 'binnedWage',
 'binnedValue',
 'binnedRelease Clause',
 'Hits'
 ]

dfNote = df_copy2[refcols]
dfNote.info()


# Duplicates
print("Duplicates in dataset:", df_copy1.duplicated().sum())

# droping duplicates 
df_clean = dfNote.drop_duplicates(inplace=False)


df_clean.duplicated().sum()


df_clean.head()


# to save to file as a csv file, use this 'pandas.to_csv()''

df_clean.to_csv('C:/Users/USER/Desktop/ONECAMPUS PROJECT 2/clean work.csv', index=False)
