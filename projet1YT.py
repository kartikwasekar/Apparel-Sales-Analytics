import pandas as pd


df = pd.read_csv('customer_shopping_behavior.csv')

print(df.head())
df.info()
print(df.describe())

print(df.isnull().sum())

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)

print(df.isnull().sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')

print(df.head())

# Create a new column
labels = ['young_adult', 'adult', 'middle_aged', 'senior']

df['age_group'] = pd.qcut(
    df['age'],
    q=4,
    labels=labels
)

print(df[['age', 'age_group']].head(10))

# Create purchase_frequency_days
frequency_mapping = {
    'Weekly': 7,
    'Fortnightly': 14,
    'Bi-Weekly': 14,
    'Monthly': 30,
    'Every 3 Months': 90,
    'Quarterly': 90,
    'Annually': 365
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(
    frequency_mapping
)

print(df[['purchase_frequency_days',
          'frequency_of_purchases']].head(10))

print(df[['discount_applied', 'promo_code_used']].head(10))

print(
    (df['discount_applied'] == df['promo_code_used']).all()
)

# Drop column
df = df.drop(columns='promo_code_used')

print(df.columns)

# Save Excel file
df.to_excel('cleaned_data1.xlsx', index=False)

