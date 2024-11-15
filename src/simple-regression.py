from pycaret import regression
import pandas as pd

df = pd.read_csv("../data/processed/integrated.csv")
regression.setup(data=df[["precipitation", "count"]], target='count', session_id=123, fold_strategy='kfold', fold=3)
best_model = regression.compare_models(include=['lr', 'ridge', 'lasso', 'en', 'huber'])
slope = best_model.coef_[0]
intercept = best_model.intercept_
latex_string = f"$\\widehat{{count}} = {slope} \\cdot precipitation + {intercept}$"

with open("../results/regression-output.md", "w") as file:
    file.write(latex_string)