# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap

# Defining a function to read CSV files


def readfile(filename):
    data = pd.read_csv(filename, sep=',', skiprows=4)
    return data


# Calling the function
ele_data1 = readfile('API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_6300057.csv')
gdp_data = readfile('API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_6298243.csv')
source_data = readfile('API_19_DS2_en_csv_v2_6300757.csv')
mob_data = readfile('API_IT.CEL.SETS.P2_DS2_en_csv_v2_6299899.csv')

# Dropping the unwanted columns from dataset
ele_data_ = ele_data1.drop(
    ['Country Code', 'Indicator Code', 'Unnamed: 67'], axis=1)
ele_data_

# Opting selective countries and data cleaining
countries = ['Australia', 'Brazil', 'Canada', 'China',
             'India', 'Japan', 'United States', 'World']
ele_data_y = ele_data_[ele_data_["Country Name"].isin(countries)]
ele_data_y = ele_data_y.drop(['1960', '1961', '1962', '1963', '1964', '1965',
                              '1966', '1967', '1968', '1969', '1970', '2015',
                              '2016', '2017', '2018', '2019', '2020', '2021',
                              '2022'], axis=1)

# Selecting particular countries and dropping unwanted columns
gdp_data1 = gdp_data[gdp_data["Country Name"].isin(countries)]
gdp_data1 = gdp_data1.drop(
    ['Country Code', 'Indicator Code', 'Indicator Name', '1960',
     'Unnamed: 67'], axis=1)

# Selecting and sorting required data
source_data1 = source_data[source_data["Country Name"].isin(countries)]

# Selecting Specific indicator for source_data
source_data_urban = source_data1[source_data1['Indicator Name']
                                 == 'Urban population (% of total population)']
source_data_urban = source_data_urban.drop(
    ['Country Code', 'Indicator Code', 'Unnamed: 67', 'Indicator Name'],
    axis=1)
source_data_urban.set_index('Country Name', inplace=True, drop=True)
source_data_urban

# Transposing the data
source_data_urban_t = source_data_urban.T.rename_axis('Years')

# Creating a 2x2 grid of subplots for visualizations
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(
    18, 14), gridspec_kw={'hspace': 0.4}, facecolor='yellow')
fig.patch.set_facecolor('yellow')

# Creating an area plot for urban population percentage over time
source_data_urban_t.plot(kind='area', alpha=0.6, fontsize=16, ax=axes[0, 0])

# Adding labels and title to the subplot with font size
axes[0, 0].set_xlabel('Years', fontsize=18)
axes[0, 0].set_ylabel('Population in %', fontsize=18)
axes[0, 0].set_title('Urban population (% of total population)', fontsize=18)

# Adding a legend with 2 columns and adjusting font size
axes[0, 0].legend(ncol=2, fontsize=12)

# Setting the background color of the subplot
axes[0, 0].set_facecolor('yellow')


# Selecting and sorting required data
mob_data = mob_data[mob_data["Country Name"].isin(countries)]
mob_data = mob_data.drop(['Country Code', 'Indicator Code', 'Indicator Name', 'Unnamed: 67', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967',
                         '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1981', '1982', '1983', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], axis=1)

# Selecting specific columns form dataframe
df_selected_years = ele_data_y[['Country Name',
                                'Indicator Name', '1974', '1994', '2014']]

# Melting the dataframe to reshappe it
df_selected_years_melted = pd.melt(df_selected_years, id_vars=[
                                   'Country Name', 'Indicator Name'], var_name='Year', value_name='Value')

# Ploting bar plot and adding labels, title and legend with fontsize
sns.barplot(x='Value', y='Country Name', hue='Year',
            data=df_selected_years_melted, dodge=True, ax=axes[1, 0])
axes[1, 0].set_title(
    'Electric power consumption for Years 1974, 1994, and 2014', fontsize=16)
axes[1, 0].set_xlabel(
    'Electric power consumption (kWh per capita)', fontsize=18)
axes[1, 0].set_ylabel('Country Name', fontsize=18)
axes[1, 0].legend(title='Year', fontsize=14)

# Adjusting tick parameters for both x and y axes in the subplot
axes[1, 0].tick_params(axis='x', labelsize=16)
axes[1, 0].tick_params(axis='y', labelsize=16)

# Setting the background color of the subplot
axes[1, 0].set_facecolor('yellow')

# Transposing mob_data
mob_data_t = mob_data.T
mob_data_t.columns = mob_data_t.iloc[0]
mob_data_t = mob_data_t.iloc[1:]
mob_data_t.index = pd.to_numeric(mob_data_t.index)
mob_data_t['Years'] = mob_data_t.index
mob_data_t.reset_index(inplace=True)
mob_data_t = mob_data_t.drop(['index'], axis=1)

# Plotting the line plot and adding labels, title and legend
axes[0, 1].plot(mob_data_t['Years'], mob_data_t['Australia'],
                color='cyan', label='Australia', marker='*')
axes[0, 1].plot(mob_data_t['Years'], mob_data_t['Brazil'],
                color='r', label='Brazil', marker='*')
axes[0, 1].plot(mob_data_t['Years'], mob_data_t['Canada'],
                color='k', label='Canada', marker='*')
axes[0, 1].plot(mob_data_t['Years'], mob_data_t['China'],
                color='y', label='China', marker='*')
axes[0, 1].plot(mob_data_t['Years'], mob_data_t['India'],
                color='g', label='India', marker='*')
axes[0, 1].plot(mob_data_t['Years'], mob_data_t['Japan'],
                color='b', label='Japan', marker='*')
axes[0, 1].plot(mob_data_t['Years'], mob_data_t['United States'],
                color='m', label='United States', marker='*')
axes[0, 1].set_xlabel("Years", fontsize=18)
axes[0, 1].set_ylabel("Subscriptions", fontsize=18)
axes[0, 1].set_title(
    "Mobile cellular subscriptions (per 100 people) over the years", fontsize=18)
axes[0, 1].legend(fontsize=14)

# Adjusting tick parameters for both x and y axes in the subplot
axes[0, 1].tick_params(axis='x', labelsize=16)
axes[0, 1].tick_params(axis='y', labelsize=16)

# Setting the background color of the subplot
axes[0, 1].set_facecolor('yellow')

# Transposing gdp_data1
gdp_data1.t = gdp_data1.T
gdp_data1.t.columns = gdp_data1.t.iloc[0]
gdp_data1.t = gdp_data1.t.iloc[1:]
gdp_data1.t.index = pd.to_numeric(gdp_data1.t.index)
gdp_data1.t['Years'] = gdp_data1.t.index
gdp_data1.t.reset_index(inplace=True)

# Select specific years
sel_years = ['1961', '1971', '1981', '1991', '2001', '2011', '2021']
gdp_data1.t[gdp_data1.t['Years'].isin(sel_years)]
gdp_data1.t_y = gdp_data1.t[gdp_data1.t["Years"].astype(str).isin(sel_years)]

# Plotting line plot with labels, title and legend
axes[1, 1].plot(gdp_data1.t_y['Years'], gdp_data1.t_y['Australia'],
                color='cyan', label='Australia')
axes[1, 1].plot(gdp_data1.t_y['Years'], gdp_data1.t_y['India'],
                color='g', label='India')
axes[1, 1].plot(gdp_data1.t_y['Years'], gdp_data1.t_y['United States'],
                color='m', label='United States')
axes[1, 1].plot(gdp_data1.t_y['Years'], gdp_data1.t_y['World'],
                color='r', label='World', marker='*')
axes[1, 1].set_xlabel("Years", fontsize=18)
axes[1, 1].set_ylabel("GDP growth (annual %)", fontsize=18)
axes[1, 1].set_title(
    "GDP growth (annual %) for 10 consecutive years form 1961 to 2021", fontsize=16)
axes[1, 1].legend(fontsize=14)

# Adjusting tick parameters for both x and y axes in the subplot
axes[1, 1].tick_params(axis='x', labelsize=16)
axes[1, 1].tick_params(axis='y', labelsize=16)

# Setting the background color of the subplot
axes[1, 1].set_facecolor('yellow')

# Creating a dictionary for student information box style
student_info = dict(boxstyle='round', facecolor='blue', alpha=0.5)

# Adding text to the plot with name and ID number
plt.text(0.50, -0.09, 'Student Name: Sohan Kumar Narayanaswamy', fontsize=20,
         color='black', ha='center', va='center', transform=fig.transFigure, bbox=student_info)
plt.text(0.50, -0.12, 'Student ID: 22085239', fontsize=20, color='black',
         ha='center', va='center', transform=fig.transFigure, bbox=student_info)

# Adding main heading of the plot
plt.suptitle("Comprehensive Analysis of Country Development (1960 - 2022)", fontsize=35,
             fontweight='heavy', backgroundcolor='blue', color='White', bbox=dict(facecolor='blue', edgecolor='black', boxstyle='round,pad=0.6'))

# Creating a text box for adding information
plot_info = '''The dashboard analyses the growth of the countries between 1960
 to 2022.In the urban population plot, we can see a massive increase in 
 population with overall of 40.93% and this shows many people has shift to
 urban from rural to improve there standard of living. This causes the average 
 number of mobile phone subscribers to increase by 95 per 100 individuals.
Its extremely evident that the usage of power has climbed to aprox 61.5% across
 the world, when compared between year 1974 and 2014. However a country is 
 believed to be developed when the GDP growth is positive as is reflected in 
 the 4th plot.The growth of gdp from year 1961 to 2021 is 38.9%, which is a
 decent growth.'''
info = textwrap.fill(plot_info, width=125,
                     initial_indent='', subsequent_indent='')

# Adding the information text to the plot
plot_info_box = dict(boxstyle='round', facecolor='white',
                     edgecolor='black', alpha=0.7, pad=0.5)
plt.text(0.5, 0.0, info, fontsize=22, color='k',
         ha='center', va='center', transform=fig.transFigure, bbox=plot_info_box)

# Saving the plot as an image with good resolution
plt.savefig("22085239.png", dpi=300)
