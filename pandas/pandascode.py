import pandas as pd

# Creating Smartphone Sales Dataset
data = {
    'Model': ['Galaxy A55', 'iPhone 15', 'OnePlus 12', 'Pixel 8',
              'Redmi Note 13', 'Vivo V30', 'Nothing Phone 2', 'Realme 12'],

    'Brand': ['Samsung', 'Apple', 'OnePlus', 'Google',
              'Xiaomi', 'Vivo', 'Nothing', 'Realme'],

    'Price': [38000, 70000, 58000, None, 22000, 32000, None, 18000],

    'Units_Sold': [120, 95, None, 80, 150, None, 70, 180],

    'Rating': [4.3, 4.6, 4.5, None, 4.1, 4.2, 4.4, None]
}

df = pd.DataFrame(data)

# Display original dataset
print("========== ORIGINAL DATASET ==========")
print(df)


# --------------------------------------------------
# 1. DETECT MISSING VALUES
# --------------------------------------------------

print("\n========== 1. DETECT MISSING VALUES ==========")

print(df.isnull())


# --------------------------------------------------
# 2. COUNT MISSING VALUES
# --------------------------------------------------

print("\n========== 2. COUNT MISSING VALUES ==========")

print(df.isnull().sum())


# --------------------------------------------------
# 3. REMOVE MISSING VALUES
# --------------------------------------------------

print("\n========== 3. REMOVING MISSING VALUES ==========")

df_removed = df.dropna()

print(df_removed)


# --------------------------------------------------
# 4. FILLING MISSING VALUES
# --------------------------------------------------

print("\n========== 4. FILLING MISSING VALUES ==========")

df_filled = df.copy()

# Fill Price with average price
df_filled['Price'] = df_filled['Price'].fillna(
    df_filled['Price'].mean()
)

# Fill Units Sold with average units sold
df_filled['Units_Sold'] = df_filled['Units_Sold'].fillna(
    df_filled['Units_Sold'].mean()
)

# Fill Rating with average rating
df_filled['Rating'] = df_filled['Rating'].fillna(
    df_filled['Rating'].mean()
)

print(df_filled)


# --------------------------------------------------
# 5. GROUPING DATA
# --------------------------------------------------

print("\n========== 5. GROUPING DATA ==========")

# Group by Brand and calculate average price
brand_group = df_filled.groupby('Brand')['Price'].mean()

print("\nAverage Price by Brand:")
print(brand_group)


# Group by Brand and calculate total units sold
sales_group = df_filled.groupby('Brand')['Units_Sold'].sum()

print("\nTotal Units Sold by Brand:")
print(sales_group)


# Group by Brand and calculate average rating
rating_group = df_filled.groupby('Brand')['Rating'].mean()

print("\nAverage Rating by Brand:")
print(rating_group)


# --------------------------------------------------
# FINAL DATASET
# --------------------------------------------------

print("\n========== FINAL DATASET ==========")
print(df_filled)
