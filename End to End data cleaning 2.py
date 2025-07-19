
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

# calling / reading the data
df = pd.read_csv(r'C:\Users\USER\Desktop\ONECAMPUS PROJECT 2\clean work.csv')

df
df.info()

"""#DISTRIBUTION
import matplotlib.pyplot as plt
df.plot(kind = 'density', subplots = True, layout = (12,8), sharex = False)
plt.gcf().set_size_inches(20,20)
plt.show()"""

"""import matplotlib.pyplot as plt
df.plot(kind = 'box', subplots = True, layout = (16,8), sharex = False)
plt.gcf().set_size_inches(20,20)
plt.show()"""

continuous_vars=df.select_dtypes('float64').columns
print(continuous_vars)
continuous_vars1=df.select_dtypes('int64').columns
print(continuous_vars1)
categorical_vars=df.select_dtypes('object').columns
print(categorical_vars)

df.describe()
df_cat = df.select_dtypes(object)
df_num = df.select_dtypes(np.number)

df_cat

df_num

"""#canva plot of data code...
import seaborn as sn
import matplotlib.pyplot as plt

plt.figure(figsize=(50,110))
corr_matrix = df_num.corr(numeric_only=True)
sn.heatmap(corr_matrix, annot=True)
plt.show()"""

"""import numpy as np
matrix = np.triu(df.corr())
plt.figure(figsize = (50,200))
sn.heatmap(df.corr(), annot=True, mask = matrix)"""


from sklearn.preprocessing import MinMaxScaler

# Select the numerical columns from your DataFrame
numerical_cols = ['↓OVA', 'POT', 'Attacking', 'Crossing', 'Finishing', 'Heading Accuracy',
       'Volleys', 'Skill', 'Curve', 'FK Accuracy', 'Long Passing',
       'Ball Control', 'Movement', 'Acceleration', 'Sprint Speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot Power', 'Jumping', 'Stamina',
       'Strength', 'Long Shots', 'Mentality', 'Interceptions', 'Positioning',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'Total Stats', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Value', 'Wage', 'Release Clause', 'Dribbling',
       'Short Passing','Age', 'BOV', 'Aggression', 'Vision', 'GK Reflexes', 'Base Stats', 'LM',
       'CDM', 'CM', 'LWB', 'RW', 'LB', 'RWB', 'RB', 'GK', 'RM', 'CB', 'ST',
       'CAM', 'LW', 'CF', 'Weight', 'Height', 'W/F', 'SM', 'IR']

# Create a new DataFrame with only the numerical columns
df_numeric = df[numerical_cols]

# Normalize the numerical data
scaler = MinMaxScaler()
df_numeric_rescaled = scaler.fit_transform(df_numeric)

# Replace the original numerical columns with the normalized columns
df[numerical_cols] = df_numeric_rescaled

df_numeric_rescaled

# converting the rescaled X to a dataframe and adding back Y

df_numeric_rescaledX = pd.DataFrame(df_numeric_rescaled, columns =['↓OVA', 'POT', 'Attacking', 'Crossing', 'Finishing', 'Heading Accuracy',
       'Volleys', 'Skill', 'Curve', 'FK Accuracy', 'Long Passing',
       'Ball Control', 'Movement', 'Acceleration', 'Sprint Speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot Power', 'Jumping', 'Stamina',
       'Strength', 'Long Shots', 'Mentality', 'Interceptions', 'Positioning',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'Total Stats', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Value', 'Wage', 'Release Clause', 'Dribbling',
       'Short Passing','Age', 'BOV', 'Aggression', 'Vision', 'GK Reflexes', 'Base Stats', 'LM',
       'CDM', 'CM', 'LWB', 'RW', 'LB', 'RWB', 'RB', 'GK', 'RM', 'CB', 'ST',
       'CAM', 'LW', 'CF', 'Weight', 'Height', 'W/F', 'SM', 'IR'])
# adding back the outcome column

print(df_numeric_rescaledX)
df_numeric_rescaledX['Hits'] = df['Hits']
print(df_numeric_rescaledX)

df_numeric_rescaledX.Weight.plot(kind='density')

from sklearn.preprocessing import StandardScaler

# Select the numerical columns from your DataFrame
numerical_cols = ['↓OVA', 'POT', 'Attacking', 'Crossing', 'Finishing', 'Heading Accuracy',
       'Volleys', 'Skill', 'Curve', 'FK Accuracy', 'Long Passing',
       'Ball Control', 'Movement', 'Acceleration', 'Sprint Speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot Power', 'Jumping', 'Stamina',
       'Strength', 'Long Shots', 'Mentality', 'Interceptions', 'Positioning',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'Total Stats', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Value', 'Wage', 'Release Clause', 'Dribbling',
       'Short Passing','Age', 'BOV', 'Aggression', 'Vision', 'GK Reflexes', 'Base Stats', 'LM',
       'CDM', 'CM', 'LWB', 'RW', 'LB', 'RWB', 'RB', 'GK', 'RM', 'CB', 'ST',
       'CAM', 'LW', 'CF', 'Weight', 'Height', 'W/F', 'SM', 'IR']

# Create a new DataFrame with only the numerical columns
df_numeric_rescaledX = df[numerical_cols]

# Standardize the numerical data
scaler = StandardScaler()
df_numeric_rescaled_standardized = scaler.fit_transform(df_numeric_rescaledX)

# Replace the original numerical columns with the standardized columns
df[numerical_cols] = df_numeric_rescaled_standardized

df_numeric_rescaled_standardized

df_numeric_rescaled_standardizedY = pd.DataFrame(df_numeric_rescaled_standardized, columns =['↓OVA', 'POT', 'Attacking', 'Crossing', 'Finishing', 'Heading Accuracy',
       'Volleys', 'Skill', 'Curve', 'FK Accuracy', 'Long Passing',
       'Ball Control', 'Movement', 'Acceleration', 'Sprint Speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot Power', 'Jumping', 'Stamina',
       'Strength', 'Long Shots', 'Mentality', 'Interceptions', 'Positioning',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'Total Stats', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Value', 'Wage', 'Release Clause', 'Dribbling',
       'Short Passing','Age', 'BOV', 'Aggression', 'Vision', 'GK Reflexes', 'Base Stats', 'LM',
       'CDM', 'CM', 'LWB', 'RW', 'LB', 'RWB', 'RB', 'GK', 'RM', 'CB', 'ST',
       'CAM', 'LW', 'CF', 'Weight', 'Height', 'W/F', 'SM', 'IR'])
# adding back the outcome column

print(df_numeric_rescaled_standardizedY)
df_numeric_rescaled_standardizedY['Hits'] = df['Hits']
print(df_numeric_rescaled_standardizedY)

df_numeric_rescaled_standardizedY.describe().T

df_numeric_rescaled_standardizedY.Weight.plot(kind='density')

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer

# Select the numerical columns from your DataFrame
numerical_cols = ['↓OVA', 'POT', 'Attacking', 'Crossing', 'Finishing', 'Heading Accuracy',
       'Volleys', 'Skill', 'Curve', 'FK Accuracy', 'Long Passing',
       'Ball Control', 'Movement', 'Acceleration', 'Sprint Speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot Power', 'Jumping', 'Stamina',
       'Strength', 'Long Shots', 'Mentality', 'Interceptions', 'Positioning',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'Total Stats', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Value', 'Wage', 'Release Clause', 'Dribbling',
       'Short Passing','Age', 'BOV', 'Aggression', 'Vision', 'GK Reflexes', 'Base Stats', 'LM',
       'CDM', 'CM', 'LWB', 'RW', 'LB', 'RWB', 'RB', 'GK', 'RM', 'CB', 'ST',
       'CAM', 'LW', 'CF', 'Weight', 'Height', 'W/F', 'SM', 'IR']

# Create a new DataFrame with only the numerical columns
df_numeric_rescaled_standardizedY = df[numerical_cols]
#print(df_numeric_rescaled_standardized)
# Normalize the numerical data
scaler = Normalizer().fit(df_numeric_rescaled_standardizedY)
df_numeric_rescaled_standardized_normalized = scaler.transform(df_numeric_rescaled_standardizedY)
#scaler = MinMaxScaler()
#df_numeric_rescaled_standardized_normalized = scaler.fit_transform(df_numeric_rescaled_standardizedY)
#print(df_numeric_rescaled_standardized_normalized)
# Replace the original numerical columns with the normalized columns
df[numerical_cols] = df_numeric_rescaled_standardized_normalized

df_numeric_rescaled_standardized_normalized

df_numeric_rescaled_standardized_normalizedZ = pd.DataFrame(df_numeric_rescaled_standardized_normalized, columns =['↓OVA', 'POT', 'Attacking', 'Crossing', 'Finishing', 'Heading Accuracy',
       'Volleys', 'Skill', 'Curve', 'FK Accuracy', 'Long Passing',
       'Ball Control', 'Movement', 'Acceleration', 'Sprint Speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot Power', 'Jumping', 'Stamina',
       'Strength', 'Long Shots', 'Mentality', 'Interceptions', 'Positioning',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'Total Stats', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Value', 'Wage', 'Release Clause', 'Dribbling',
       'Short Passing','Age', 'BOV', 'Aggression', 'Vision', 'GK Reflexes', 'Base Stats', 'LM',
       'CDM', 'CM', 'LWB', 'RW', 'LB', 'RWB', 'RB', 'GK', 'RM', 'CB', 'ST',
       'CAM', 'LW', 'CF', 'Weight', 'Height', 'W/F', 'SM', 'IR'])
# adding back the outcome column

print(df_numeric_rescaled_standardized_normalizedZ)
df_numeric_rescaled_standardized_normalizedZ['Hits'] = df['Hits']
print(df_numeric_rescaled_standardized_normalizedZ)
df_numeric_rescaled_standardized_normalizedZ.describe().T

dfFitted = df_numeric_rescaled_standardized_normalizedZ.Weight.plot(kind='density')
dfFitted

def outlier_lims(col):
    q3,q1 = np.percentile(col, [75,25])
    iqr = q3-q1
    upper_lim = q3 + 1.5*iqr
    lower_lim = q1 - 1.5*iqr
    return upper_lim, lower_lim

for col in df_numeric_rescaled_standardized_normalizedZ:
    print("--------------------------------------------------")
    print("Column:", col)
    
    UL,LL = outlier_lims(df[col])
    print("Upper Limit =", UL)
    print("Lower Limit =", LL)
    
    total_outliers = len(df.loc[df[col]<LL,col]) + len(df.loc[df[col]>UL,col])
    percent = (total_outliers / len(df.index) )*100
    
    print("Percentage of Outliers=", percent)
    print("-------------------------------------------------- \n")


df.loc[df[col]<LL]

df.loc[df[col]>UL]


# Get the maximum number of rows and columns that can be displayed
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

import numpy as np

# Select float and integer columns
df.select_dtypes(include=[np.number]).skew()

#using log transformation for PhysicalHealth and MentalHealth to reduce skewness
df[['Value', 'Wage','Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning','Release Clause',
       'GK Reflexes','IR','RW','LB','CF','CDM','GK','LWB','RM','RB','CAM','LM','LW','RWB']] = np.log1p(df[['Value', 'Wage','Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning','Release Clause',
       'GK Reflexes','IR','RW','LB','CF','CDM','GK','LWB','RM','RB','CAM','LM','LW','RWB']])

import numpy as np

# Select float and integer columns
dfposh= df.select_dtypes(include=[np.number]).skew()
dfposh

# TESTING THE MODEL
from sklearn.linear_model import LinearRegression
# Building a model...
X =df[['↓OVA', 'POT', 'Attacking', 'Crossing', 'Finishing', 'Heading Accuracy',
       'Volleys', 'Skill', 'Curve', 'FK Accuracy', 'Long Passing',
       'Ball Control', 'Movement', 'Acceleration', 'Sprint Speed', 'Agility',
       'Reactions', 'Balance', 'Power', 'Shot Power', 'Jumping', 'Stamina',
       'Strength', 'Long Shots', 'Mentality', 'Interceptions', 'Positioning',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'Total Stats', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Value', 'Wage', 'Release Clause', 'Dribbling',
       'Short Passing','Age', 'BOV', 'Aggression', 'Vision', 'GK Reflexes', 'Base Stats', 'LM',
       'CDM', 'CM', 'LWB', 'RW', 'LB', 'RWB', 'RB', 'GK', 'RM', 'CB', 'ST',
       'CAM', 'LW', 'CF', 'Weight', 'Height', 'W/F', 'SM', 'IR']].values
Y =df[['Hits']].values

model = LinearRegression()
pred = model.fit(X,Y)
score = model.score(X,Y)
score


# In this case, an R-squared value of 0.19335889369778703 suggests that the independent variables in the model explain only about 19% of the variance in the target variable (Hits). This means that there is still a lot of unexplained variability in the target variable that is not captured by the independent variables in the model.
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Clean the 'Hits_y' column and convert all values to string
df['Hit'] = df['Hits'].astype(str)

# include 'PAS', 'SHO', 'PAS', 'DRI', and 'DEF' columns as features:
selected_features = ['Age', '↓OVA', 'POT', 'PAC', 'Hits', 'PAS', 'SHO','DRI', 'DEF', 'PHY', 'Movement',
                   'Best Position', 'Attacking', 'Crossing', 'Finishing','Stamina','Heading Accuracy']
X = df[selected_features]

# Convert the categorical target variable 'Hits_y' into numerical labels
label_encoder = LabelEncoder()
Y_encoded = label_encoder.fit_transform(df['Hits'])

# Scale the input features to the range [0, 1]
scaler = MinMaxScaler()
#X_scaled = scaler.fit_transform(X)
df_numeric_rescaled = scaler.fit_transform(df_numeric)


# Initialize and fit the SelectKBest feature selection
test = SelectKBest(score_func=chi2, k=5)  
fit = test.fit(df_numeric_rescaled, Y_encoded)

# Print the scores for each feature
print(fit.scores_)

# Transform the input data to keep only the selected features
X_selected = fit.transform(df_numeric_rescaled)
from sklearn.model_selection import train_test_split  # Import the train_test_split function


# Step 2: Data Splitting
X = df.drop('Hits', axis=1)  # Features
y = df['Hits']               # Target variable

X_train, X_test, Y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# One-hot encode the 'Best Position' column
X_encoded = pd.get_dummies(X, columns=['Best Position'])

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y, test_size=0.2, random_state=42)

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict the number of hits for the test set
Y_pred = model.predict(X_test)
# Print the predicted number of hits for each player in the test set
print("Predicted number of hits for each player:")
print(Y_pred)


# Calculate the mean squared error (MSE) and R-squared (R2) to evaluate the model
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

# Calculate the accuracy of the model (percent of correctly predicted values)
accuracy = model.score(X_test, Y_test) * 100
print("Model Accuracy:", accuracy, "%")


# This code performs linear regression to predict the number of hits based on the features provided in the dataset.
# Here's a breakdown of what the code does:
# One-hot encoding: The code uses the pd.get_dummies() function from the pandas library to perform one-hot encoding on the 'Best Position' column of the input data X. One-hot encoding converts categorical variables into binary vectors, which can be used as input for machine learning algorithms.
# Data splitting: The code then splits the encoded data (X_encoded) and the corresponding target variable (Y) into training and testing sets using the train_test_split() function from the scikit-learn library. The testing set size is set to 20% of the total data, and a random seed of 42 is used for reproducibility.
# Model initialization and training: The code initializes a linear regression model using the LinearRegression() class from scikit-learn. It then fits (trains) the model on the training data (X_train, Y_train) using the fit() method.
# Prediction: The code uses the trained model to predict the number of hits for the test set (X_test) using the predict() method. The predicted values are stored in the Y_pred variable.
# Model evaluation: The code calculates the mean squared error (MSE) and R-squared (R2) to evaluate the performance of the model. The mean squared error measures the average squared difference between the predicted and actual values, while the R-squared score indicates the proportion of the variance in the target variable that can be explained by the model.
# Model accuracy: The code calculates the accuracy of the model by calling the score() method on the model with the test data (X_test, Y_test). The score() method returns the coefficient of determination (R2 score) for the regression model, which represents the proportion of the variance in the target variable that the model explains. The accuracy is then multiplied by 100 to convert it to a percentage.
# Finally, the code prints the MSE, R2 score, and model accuracy to the console.
