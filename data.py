import pandas as pd
import random

data = []
for i in range(100):
    data.append({
        'age': random.randint(18, 80),
        'location': random.choice(['Urban', 'Rural']),
        'language': random.choice(['Hindi', 'English']),
        'success': random.choice([True, False])
    })

df = pd.DataFrame(data)
df.to_csv('mock_data.csv', index=False)
print("Data saved!")
