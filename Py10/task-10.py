
import random
import pandas as pd

data = pd.DataFrame(random.sample(['black', 'white']*10, 20) ,columns={'Colors'})
data.head()
print(data)