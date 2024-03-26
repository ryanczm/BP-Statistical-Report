import pandas as pd
import pickle

colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'cyan', 'magenta', 'yellow']

region_to_countries = {

    'North America':
                                 ['USA', 'Canada', 'Mexico', 'US'],
    'Central & South America': 
                                ['Argentina', 'Brazil', 'Bolivia' ,'Chile', 'Colombia', 'Ecuador', 'Peru', 'Trinidad & Tobago', 'Venezuela', 'Central America', 'Other Caribbean', 'Other South America', 'Other S. & Cent. America', 
                                 'S. & Cent. America', 'Curacao', 'Netherlands Antilles', 'Other Americas'],

    'Europe':                   [
                                'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
                                'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
                                'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
                                'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
                                'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Other Europe',
                                'United Kingdom', 'Europe', 'European Union', 'Rest of Europe', 'Other EU' 
                                ],
    'CIS': 
                                ['Azerbaijan','Belarus', 'Kazakhstan','Russian Federation', 'Turkmenistan', 'USSR','Uzbekistan', 'Other CIS', 'CIS'],
    'Asia Pacific': 
                                ['China', 'Japan', 'India', 'Australia', 'Brunei','China','Indonesia','Malaysia','Thailand','Vietnam','Other Asia Pacific', 'Bangladesh','China Hong Kong SAR',
                                 'New Zealand', 'Philippines', 'Pakistan', 'South Korea', 'Sri Lanka', 'Taiwan', 'Myanmar','Papua New Guinea','Brunei', 'Singapore'],
    'Africa': 
                                ['Algeria', 'Egypt','Morocco', 'South Africa','Eastern Africa', 'Middle Africa', 'Western Africa', 'Other Northern Africa', 'Other Southern Africa', 
                                 'Angola', 'Chad', 'Republic of Congo','Egypt', 'Equatorial Guinea','Gabon', 'Libya','Nigeria','South Sudan','Sudan','Tunisia','Other Africa', 'Africa'],
    'Middle East': 
                                ['Iran', 'Iraq','Israel', 'Kuwait','Oman', 'Qatar', 'Saudi Arabia', 'United Arab Emirates','Other Middle East', 'Bahrain', 'Yemen', 'Syria', 'Other Middle East & Africa', 'Middle East']
}


def map_to_region(country):
    for region, countries in region_to_countries.items():
        if country in countries:
            return region
    return 'Unknown'


oil_tabs = ["Energy Cons", "Energy Cons Fuel 2022", "Oil Reserves", "Oil Production", "Liquids Consumption", "Product Regional Consumption", 
                    "Spot Crude Prices", "Capacity", "Throughput", "Margins", "Crude Import Export", "Crude Movement 2022", "Product Movement 2022"]

gas_tabs = ["Gas Reserves", "Gas Production", "Gas Consumption", "Gas Prices", "Gas Imports Exports", "LNG Exports", "LNG Imports", "Pipeline Trade Movements"]

oil_path = 'BP-Statistical-Review-2022-Crude.xlsx'
gas_path = 'BP-Statistical-Review-2022-Gas.xlsx'

def create_dfs(fp, tabs, load_pickle=False):

    if 'Crude'in fp:
        name = 'crude'
    if 'Gas' in fp:
        name = 'gas'

    if load_pickle:
        with open(f'{name}.pkl', 'rb') as handle:
            dfs = pickle.load(handle)
    else:
        xls = pd.ExcelFile(fp)
        dfs = {}
        for sheet_name in xls.sheet_names:
            df = xls.parse(sheet_name, header=0)
            if df.columns[0] == 'Country':        
                df['Continent'] = df['Country'].apply(map_to_region)
                if 'Product' in df.columns:
                    df.set_index(['Continent', 'Country', 'Product'], inplace=True)
                elif 'Type' in df.columns:
                    df.set_index(['Continent', 'Country', 'Type'], inplace=True)
                else:
                    df.set_index(['Continent', 'Country'], inplace=True)
            elif 'Region' in df.columns:
                if 'Type' in df.columns:
                    df.set_index(['Region','Type'], inplace=True)
                else:
                    df.set_index(['Region'], inplace=True)
            elif df.columns[0] == 'Year':
                df.set_index(['Year'], inplace=True)
                
    
            if 'Thousand barrels daily' in df.columns:
                df.drop(columns=['Thousand barrels daily'],inplace=True)
            dfs[sheet_name] = df

        with open(f'{name}.pkl', 'wb') as handle:
            pickle.dump(dfs, handle)

    for tab in tabs:
        var_name = tab.lower().replace(' ', '_')
        globals()[var_name] = dfs[tab]

    return 0

