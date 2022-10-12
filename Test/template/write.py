import pandas as pd
from datetime import datetime

def make_test_csv(index, OimgName, imgName, imgPath, imgID, gCode):
    new_line = pd.DataFrame([[index, OimgName, imgName, imgPath, imgID, gCode]], 
                            columns = ["ind", "Oimg", "iN", "iP", "iID", "gC"])
    new_line.to_csv('apply.csv', mode = "a", header = False)