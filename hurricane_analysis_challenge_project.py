# write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. 
# Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# 1
# write your update damages function here:
# Write a function that returns a new list of updated damages where the recorded data is converted to float values
# and the missing data is retained as "Damages not recorded".
conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
def convert_damages(damages, conversion):
  for record in damages:
    if record[-1] == "M":
      new_value = float(record[:-1]) * conversion.get("M")
    elif record[-1] == "B":
      new_value = float(record[:-1]) * conversion.get("B")
    else:
      new_value = record
    updated_damages.append(new_value)
  return updated_damages 
convert_damages(damages, conversion)


# 2
# write your construct hurricane dictionary function here:
# Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes,
# and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, # Damage, Death) about the hurricane.

hurricanes = {}
def create_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  
  for i in range(len(names)):
    hurricanes[names[i]] = {"Name": names[i],
    "Month": months[i],
    "Year": years[i],
    "Max Sustained Wind": max_sustained_winds[i],
    "Areas Affected": areas_affected[i],
    "Damage": updated_damages[i],
    "Deaths": deaths[i]}
    
  return hurricanes
  
create_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


# 3
# write your construct hurricane by year dictionary function here:
hurricanes_year = {}
def hurricane_by_year(hurricanes):
  for name in hurricanes.values():
    current_year = name['Year']
    current_hurricane = name
    if current_year not in hurricanes_year:
      hurricanes_year[current_year] = [current_hurricane]
    else:
       hurricanes_year[current_year].append(current_hurricane)
  
  return hurricanes_year
hurricane_by_year(hurricanes)


# 4
# create dictionary of areas to store the number of hurricanes involved in
# write your count affected areas function here:
affected_areas_count = dict()
def Counting_damaged_areas(hurricanes):
   for info in hurricanes:
    for area in hurricanes[info]['Areas Affected']:
      if area not in affected_areas_count:
        affected_areas_count[area] = 1
      else:
        affected_areas_count[area] += 1
  
  return(affected_areas_count)
Counting_damaged_areas(hurricanes)


# 5
# write your find most affected area function here:
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def max_area_count(affected_areas_count):
  max_area = ''
  max_area_count = 0
  for area in affected_areas_count:
    if max_area_count < affected_areas_count[area] :
      max_area = area
      max_area_count = affected_areas_count[area]
    
  return(max_area, max_area_count)
max_area_count(affected_areas_count)


# 6
# write your greatest number of deaths function here:
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def calculate_mortality(hurricanes):
  max_mortality_name = ''
  max_mortality = 0
  for name in hurricanes:
    if max_mortality < hurricanes[name]['Deaths']:
      max_mortality_name = name
      max_mortality = hurricanes[name]['Deaths']
   
  return(max_mortality_name, max_mortality)
calculate_mortality(hurricanes)


# 7
# categorize hurricanes in new dictionary with mortality severity as key
# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
def hurricanes_mortality(hurricanes):
  for hurricane in hurricanes:
    deaths = hurricanes[hurricane]['Deaths']
    
    if deaths < mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[hurricane])
    
    elif deaths > mortality_scale[0] and deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[hurricane])

    elif deaths > mortality_scale[1] and deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[hurricane])

    elif deaths > mortality_scale[2] and deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[hurricane])  

    elif deaths > mortality_scale[3] and deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[hurricane])
 
   return(hurricanes_by_mortality)
hurricanes_mortality(hurricanes)



# 8
# write your greatest damage function here:
# Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def hurricanes_max_damage(hurricanes):
  max_damage_name = ''
  max_damage = 0

  for name in hurricanes:
    if hurricanes[name]['Damage'] != "Damages not recorded":
      if max_damage < hurricanes[name]['Damage']:
        max_damage_name = hurricanes[name]['Name']
        max_damage = hurricanes[name]['Damage']
  
  return(max_damage_name, max_damage)
hurricanes_max_damage(hurricanes)


# 9
# write your catgeorize by damage function here:
# Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def hurricanes_damage_scale(hurricanes):
  hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  
  for hurricane in hurricanes:
    if hurricanes[hurricane]['Damage'] != "Damages not recorded":
      if hurricanes[hurricane]['Damage'] > damage_scale[0] and hurricanes[hurricane]['Damage'] == damage_scale[0]:
        hurricanes_by_damage[0] = hurricanes[hurricane]

      elif hurricanes[hurricane]['Damage'] > damage_scale[0] and hurricanes[hurricane]['Damage'] <= damage_scale[1]:
        hurricanes_by_damage[1] = hurricanes[hurricane]
      
      elif hurricanes[hurricane]['Damage'] > damage_scale[1] and hurricanes[hurricane]['Damage'] <= damage_scale[2]:
        hurricanes_by_damage[2] = hurricanes[hurricane]

      elif hurricanes[hurricane]['Damage'] > damage_scale[2] and hurricanes[hurricane]['Damage'] <= damage_scale[3]:
        hurricanes_by_damage[3] = hurricanes[hurricane]
      
      elif hurricanes[hurricane]['Damage'] > damage_scale[3] and hurricanes[hurricane]['Damage'] <= damage_scale[4]:
        hurricanes_by_damage[4] = hurricanes[hurricane]
      
      else:
        hurricanes_by_damage[5] = hurricanes[hurricane]
      
  return (hurricanes_by_damage)
hurricanes_damage_scale(hurricanes)
