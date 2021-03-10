# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_excel('./Invoice_data_Demo.xls', header=0)
for i in range(0, len(data)):
    print(data['车牌号'][i])