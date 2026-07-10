import pandas as pd
from scipy.stats import pearsonr

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("C:/Users/GUGULOTH/OneDrive/Documents/amazon_sales_data_story/cleaned_amazon_sales_data.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("=" * 60)
print("AMAZON SALES DATASET")
print("=" * 60)
print("Dataset Shape :", df.shape)

print("\nAvailable Columns:")
print(df.columns.tolist())

# ----------------------------------------------------------
# Automatically detect Price and Sales columns
# ----------------------------------------------------------

price_col = None
sales_col = None

for col in df.columns:
    if "price" in col.lower():
        price_col = col
    if "total" in col.lower() and "sale" in col.lower():
        sales_col = col

# Check whether columns exist
if price_col is None:
    print("\nERROR: Price column not found!")
    exit()

if sales_col is None:
    print("\nERROR: Total Sales column not found!")
    exit()

print("\nUsing Columns:")
print("Price Column :", price_col)
print("Sales Column :", sales_col)

# ----------------------------------------------------------
# Select Variables
# ----------------------------------------------------------

price = df[price_col]
sales = df[sales_col]

# ----------------------------------------------------------
# Hypothesis
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("STATISTICAL HYPOTHESIS TESTING")
print("=" * 60)

print("\nNull Hypothesis (H0):")
print("There is NO significant relationship between Product Price and Total Sales.")

print("\nAlternative Hypothesis (H1):")
print("There IS a significant relationship between Product Price and Total Sales.")

# ----------------------------------------------------------
# Pearson Correlation Test
# ----------------------------------------------------------

correlation, p_value = pearsonr(price, sales)

print("\n" + "=" * 60)
print("PEARSON CORRELATION RESULT")
print("=" * 60)

print(f"Correlation Coefficient : {correlation:.4f}")
print(f"P-value                 : {p_value:.6f}")

# ----------------------------------------------------------
# Decision
# ----------------------------------------------------------

alpha = 0.05

print("\n" + "=" * 60)
print("DECISION")
print("=" * 60)

if p_value < alpha:
    print("Reject the Null Hypothesis (H0)")
    print("Result: There is a statistically significant relationship.")
else:
    print("Fail to Reject the Null Hypothesis (H0)")
    print("Result: There is NO statistically significant relationship.")

# ----------------------------------------------------------
# Interpretation
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("INTERPRETATION")
print("=" * 60)

if correlation > 0:
    print("Positive Correlation")
    print("As Product Price increases, Total Sales also tend to increase.")
elif correlation < 0:
    print("Negative Correlation")
    print("As Product Price increases, Total Sales tend to decrease.")
else:
    print("No Correlation Found")

print("\nStatistical Validation Completed Successfully!")
