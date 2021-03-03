import pandas as pd
# 20 arabalı pandas
#pd.series

arabalar =["BMW","MERCEDES","AUDI","LAMBORGHINI","BUGATTI","KOENIGSEGG","PAGANI","FORD","HONDA",
"OPEL","PEUGEOT","FERRARI","FIAT","SSANYONG","CHEVROLET","NISSAN","ROLLSROYCE","BENTLEY",
"RENAULT","DACIA"]
tablo = pd.Series(arabalar)
print(tablo)