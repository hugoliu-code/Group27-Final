import global_development
import pandas as pd

dictionary_list = global_development.get_report()

flattened_dict = dict()

flattened_dict['Country'] = [n['Country'] for n in dictionary_list]
flattened_dict['Year'] = [n['Year'] for n in dictionary_list]

flattened_dict['Birth Rate'] = [n['Data']['Health']['Birth Rate'] for n in dictionary_list]
flattened_dict['Death Rate'] = [n['Data']['Health']['Death Rate'] for n in dictionary_list]
flattened_dict['Fertility Rate'] = [n['Data']['Health']['Fertility Rate'] for n in dictionary_list]
flattened_dict['Life Expectancy at Birth, Female'] = [n['Data']['Health']['Life Expectancy at Birth, Female'] for n in dictionary_list]
flattened_dict['Life Expectancy at Birth, Male'] = [n['Data']['Health']['Life Expectancy at Birth, Male'] for n in dictionary_list]
flattened_dict['Population Growth'] = [n['Data']['Health']['Population Growth'] for n in dictionary_list]
flattened_dict['Total Population'] = [n['Data']['Health']['Total Population'] for n in dictionary_list]

flattened_dict['Mobile Cellular Subscriptions'] = [n['Data']['Infrastructure']['Mobile Cellular Subscriptions'] for n in dictionary_list]
flattened_dict['Mobile Cellular Subscriptions per 100 People'] = [n['Data']['Infrastructure']['Mobile Cellular Subscriptions per 100 People'] for n in dictionary_list]
flattened_dict['Telephone Lines'] = [n['Data']['Infrastructure']['Telephone Lines'] for n in dictionary_list]
flattened_dict['Telephone Lines per 100 People'] = [n['Data']['Infrastructure']['Telephone Lines per 100 People'] for n in dictionary_list]


flattened_dict['Agricultural Land'] = [n['Data']['Rural Development']['Agricultural Land'] for n in dictionary_list]
flattened_dict['Agricultural Land Percent'] = [n['Data']['Rural Development']['Agricultural Land Percent'] for n in dictionary_list]
flattened_dict['Arable Land'] = [n['Data']['Rural Development']['Arable Land'] for n in dictionary_list]
flattened_dict['Arable Land Percent'] = [n['Data']['Rural Development']['Arable Land Percent'] for n in dictionary_list]
flattened_dict['Land Area'] = [n['Data']['Rural Development']['Land Area'] for n in dictionary_list]
flattened_dict['Rural Population'] = [n['Data']['Rural Development']['Rural Population'] for n in dictionary_list]
flattened_dict['Rural Population Growth'] = [n['Data']['Rural Development']['Rural Population Growth'] for n in dictionary_list]
flattened_dict['Surface Area'] = [n['Data']['Rural Development']['Surface Area'] for n in dictionary_list]


flattened_dict['Population Density'] = [n['Data']['Urban Development']['Population Density'] for n in dictionary_list]
flattened_dict['Urban Population Percent'] = [n['Data']['Urban Development']['Urban Population Percent'] for n in dictionary_list]
flattened_dict['Urban Population Percent Growth'] = [n['Data']['Urban Development']['Urban Population Percent Growth'] for n in dictionary_list]


df = pd.DataFrame(flattened_dict)
df.to_pickle("global_dev.pkl")
print(df)



