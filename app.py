# Can we predict the CO2 emission of a car based on its engine volume and weight?

import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

data = {
    'Volume': [1000, 1200, 1400, 1600, 1800, 2000, 2200],
    'Weight': [790, 850, 980, 1100, 1250, 1400, 1600],
    'CO2': [95, 99, 105, 110, 118, 125, 133]
}

df = pd.DataFrame(data)
scale = StandardScaler()
X = df[['Volume', 'Weight']]
y = df['CO2']
scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled_input = scale.transform([[1500, 1000]])
predictedCO2 = regr.predict(scaled_input)
print(f"Predicted CO2: {predictedCO2[0]}")