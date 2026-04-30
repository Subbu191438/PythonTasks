"""�� Scenario 1: Data Loading & Basic Cleaning
Understand the dataset structure and prepare it for analysis.
�� Tasks:
● Load the dataset using Pandas.
● Display:
○ First 5 rows
○ Last 5 rows
○ Column names
○ Shape of dataset
● Check data types of all columns.
● Check for missing values in:
○ Selling_Price
○ Present_Price
○ Kms_Driven
○ Fuel_Type
● Fill missing values:
○ Selling_Price → mean
○ Present_Price → mean
○ Kms_Driven → mean
○ Fuel_Type → mode
● Convert numeric columns to proper numeric type if required:
○ Selling_Price
○ Present_Price
○ Kms_Driven
○ Year
● Convert Selling_Price and Kms_Driven into NumPy arrays.
● Use NumPy to calculate:
○ minimum selling price
○ maximum selling price
○ average selling price
"""






"""
�� Scenario 2: Selling Price Trend (Line Graph)
See how selling prices vary for a small sample of cars.
�� Tasks:
● Select:
○ Car_Name
○ Selling_Price
● Take the first 10 rows only using Pandas.
● Convert Selling_Price into a NumPy array.
● Plot a line graph using Matplotlib:
○ X-axis → row index (0–9)
○ Y-axis → Selling Price
● Add:
○ title
○ x-axis label
○ y-axis label
○ markers
● Save the graph with a suitable filename."""






"""
�� Scenario 3: Expensive Cars Analysis (Filtering + Bar)
Find which fuel types are most common among expensive cars.
�� Tasks:
● Filter cars where:
○ Selling_Price > 10
● Group the filtered data by:
○ Fuel_Type
● Count number of cars in each fuel type.
● Convert:
○ fuel type labels
○ counts
into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Fuel Type
○ Y-axis → Count of expensive cars
● Add:
○ title
○ x-label
○ y-label
● Save the graph."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cardata.csv")

# Filter expensive cars
filt = df[df['Selling_Price'] > 10]

# Count cars by fuel type
fuel_counts = filt['Fuel_Type'].value_counts()

# Convert to NumPy arrays
labels = fuel_counts.index.to_numpy()
values = fuel_counts.values

# Plot bar chart
plt.bar(labels, values)
plt.title("Expensive Cars by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Count of Cars")

# Save and show
plt.savefig("expensive_cars_bar.png")
plt.show()

"""
Scenario 4: Fuel Type Distribution (Pie Chart)
Understand the overall distribution of cars by fuel type.
�� Tasks:
● Count the number of cars in each:
○ Fuel_Type
● Select all categories or top categories if needed.
● Prepare:
○ labels
○ values
● Convert values into a NumPy array.
● Plot a pie chart using Matplotlib.
● Add:
○ percentage labels
○ title
● Save the graph.
"""







"""
Scenario 5: Present Price vs Selling Price (Scatter Plot)
Check whether cars with higher present price also have higher selling price.
�� Tasks:
● Select:
○ Present_Price
○ Selling_Price
● Remove missing values if any.
● Take a smaller sample (for example first 50 or 100 rows) using Pandas.
● Convert both columns into NumPy arrays.
● Plot a scatter plot using Matplotlib:
○ X-axis → Present_Price
○ Y-axis → Selling_Price
● Add:
○ title
○ x-label
○ y-label
● Observe whether there is a positive relationship.
● Save the graph."""






"""
�� Scenario 6: Car Age Category Analysis + Bar Chart
Create a new feature using year and compare car categories.
�� Tasks:
● Create a new column using Pandas:
Car Age Category
● Year >= 2015 → "New"
● 2010 to 2014 → "Medium"
● < 2010 → "Old"
● Count number of cars in each:
○ Car Age Category
● Convert category names and counts into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Car Age Category
○ Y-axis → Count
● Add title and labels.
● Save the graph.
"""





"""
Scenario 7: Kms Driven Distribution (Histogram)
Understand how the cars are distributed based on kilometers driven.
�� Tasks:
● Select:
○ Kms_Driven
● Convert it into a NumPy array.
● Plot a histogram using Matplotlib:
○ X-axis → Kms Driven
○ Y-axis → Frequency
● Choose suitable number of bins.
● Add:
○ title
○ x-label
○ y-label
● Save the graph.
● Observe whether most cars have lower or higher mileage."""





"""
Scenario 8: Transmission-wise Selling Price Comparison
Compare average selling price for manual vs automatic cars.
�� Tasks:
● Group data by:
○ Transmission
● Calculate:
○ average Selling_Price
● Convert transmission labels and average prices into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Transmission
○ Y-axis → Average Selling Price
● Add title and labels.
● Save the graph."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cardata.csv")

# Group by Transmission and calculate average selling price
avg_price = df.groupby("Transmission")["Selling_Price"].mean()

# Convert to NumPy arrays
labels = avg_price.index.to_numpy()
values = avg_price.values

# Plot bar chart
plt.bar(labels, values)
plt.title("Average Selling Price by Transmission")
plt.xlabel("Transmission")
plt.ylabel("Average Selling Price")

# Save and show
plt.savefig("transmission_price_comparison.png")
plt.show()

"""
Scenario 9: Seller Type Analysis
Compare how many cars are sold by dealers and individuals.
�� Tasks:
● Count number of cars by:
○ Seller_Type
● Convert results into NumPy arrays.
● Plot a bar chart or pie chart using Matplotlib.
● Add labels and title.
● Save the graph.
● Identify which seller type is more common."""






"""
�� Scenario 10: Advanced Analysis + Multiple Graphs
Perform deeper analysis using Pandas, NumPy, and Matplotlib.
�� Part 1: Feature Creation
Create a new column:
Price Difference
● Price Difference = Present_Price - Selling_Price
This shows how much value the car has depreciated.
�� Part 2: NumPy Usage
● Convert Selling_Price into a NumPy array.
● Use NumPy to calculate price changes between consecutive rows using:
○ np.diff()
● Convert Price Difference column into a NumPy array.
● Find:
○ average depreciation
○ maximum depreciation
○ minimum depreciation
�� Part 3: Visualizations
�� Line Graph
● Plot Selling_Price trend for all cars.
�� Bar Chart
● Show average Selling_Price by Fuel_Type.
�� Histogram
● Plot distribution of Selling_Price.
�� Part 4: Insights
Answer these:
● Which fuel type has the highest average selling price?
● Which transmission type has higher average selling price?
● Are most cars concentrated in lower selling prices or higher selling prices?
● Do older cars tend to have lower selling prices?
�� Best Simple & Correct Columns to Use in This Dataset
These are the best columns for your tasks:
Numeric Columns
● Selling_Price
● Present_Price
● Kms_Driven
● Year
● Owner
Categorical Columns
● Fuel_Type
● Seller_Type
● Transmission
● Car_Name """
