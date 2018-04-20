import pandas as pd
import matplotlib.pyplot as plt
yelp_raw_data = pd.read_csv("/home/sijokg/PythonExamples/Yelp/yelp.csv")

print(yelp_raw_data.head())
print(yelp_raw_data.shape)
print(yelp_raw_data.isnull().sum())
print(type(yelp_raw_data))
print(type(yelp_raw_data['text']))
print(yelp_raw_data['business_id'].describe())
print(yelp_raw_data['cool'].describe())
duplicate_text = yelp_raw_data['text'].describe()['top']
print(duplicate_text)
text_is_the_duplicate = yelp_raw_data['text'] == duplicate_text
print(sum(text_is_the_duplicate))
filtered_data_frame = yelp_raw_data[text_is_the_duplicate]
print(filtered_data_frame)

stars_count_wise = yelp_raw_data['stars'].value_counts()
print(stars_count_wise)
stars_count_wise.sort_values().plot(kind='bar')

plt.show()
