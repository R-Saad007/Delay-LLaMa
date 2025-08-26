import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load & preprocess
df = pd.read_csv("flights.csv")
X = df[["HourlyDryBulbTemperature_x", "HourlyWindSpeed_x", "HourlyVisibility_x"]]
y = df["departure_delay"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Fit model
model = RandomForestRegressor()
model.fit(X_train, y_train)

print("MAE:", mean_absolute_error(y_test, model.predict(X_test)))

# Save model
import joblib
joblib.dump(model, "delay_model.pkl")
