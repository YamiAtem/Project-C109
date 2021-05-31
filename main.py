# %% [markdown]
# # ***Project C109***
# %% [markdown]
# ## Getting Reading Scores Data

# %%
import plotly.figure_factory as ff
import pandas
import plotly.graph_objects as go
import statistics
import random

data_frame = pandas.read_csv("data.csv")
data = list(data_frame["reading score"])

# %% [markdown]
# ## Calculating Mean, Median, Mode, and Standard Deviation

# %%
mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_deviation = statistics.stdev(data)

print("Statistics of the Data: ")
print(f" Mean: {mean}")
print(f" Median: {median}")
print(f" Mode: {mode}")
print(f" Standard Deviation: {std_deviation}")

# %% [markdown]
# ## Finding 3 Ranges of Standard Deviation

# %%
first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * std_deviation), mean + (2 * std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3 * std_deviation), mean + (3 * std_deviation)

# %% [markdown]
# ## Plottling Bell Curve Chart with Lines for Mean and the 3 Ranges of Standard Deviation

# %%
fig = ff.create_distplot([data], ["Reading Scores"])

# First Range of Standard Deviation
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines",              name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines",                  name="STANDARD DEVIATION 1 END"))

# Second Range of Standard Deviation
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17],                          mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines",                name="STANDARD DEVIATION 2 END"))

# Third Range of Standard Deviation
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17],                            mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines",                  name="STANDARD DEVIATION 3 END"))

# Show figure
fig.show()

# %% [markdown]
# ## Getting the Percentage of Data that lies between each standard deviation range

# %%
list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]

list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]

list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within the 1st standard deviation range".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))

print("{}% of data lies within the 2nd standard deviation range".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))

print("{}% of data lies within the 3rd standard deviation range".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))


