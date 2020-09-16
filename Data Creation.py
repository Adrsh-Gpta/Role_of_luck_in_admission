import pandas as pd
from numpy import random
import numpy as np

database = pd.DataFrame(
    columns=["Hard work", "Hard work based rank", "Hard work based result", "Luck", "Score [Hard work + luck]",
             "Luck based rank", "Luck based result", "Luck and Hard work"],
    index=range(18300))

database["Hard work"] = np.random.normal(100, 20, 18300)
database["Luck"] = np.random.normal(100, 20, 18300)

database["Hard work based rank"] = database["Hard work"].rank(ascending=False)
database["Score [Hard work + luck]"] = database.apply(lambda x: database["Hard work"] * 0.95 + database["Luck"] * 0.05)
database["Luck based rank"] = database["Score [Hard work + luck]"].rank(ascending=False)
database["Hard work based result"] = np.where(database["Hard work based rank"] <= 11, True, False)
database["Luck based result"] = np.where(database["Luck based rank"] <= 11, True, False)
database["Luck and Hard work"] = np.where(database["Hard work based result"] & database["Luck based result"], True,
                                          False)
database.to_csv("E:\PycharmProjects\Role_of_luck_in_admission\data.csv")

