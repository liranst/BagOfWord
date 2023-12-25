import pandas as pd
from BagOfWord import BagOfWord
from visualizer import Visualizer
from student import  student
import time

# Print my personal details
Liran = student(names="Liran", ids=313450264, emails="liranst13@gmail.com")
df = BagOfWord(data="hw3_dataset.csv", stopwords="stopwords.txt")
Liran.get_details()

# Output of the 20 most common words
start = time.time()
df_stack = pd.DataFrame(df.stack())

print(time.time() - start)

# Visualizer
"""df_stack.to_csv("./hw3_output.csv")
new_fig = Visualizer(data="./hw3_output.csv")
new_fig.dataset(x=df_stack.index.name, y="car", z="love")"""