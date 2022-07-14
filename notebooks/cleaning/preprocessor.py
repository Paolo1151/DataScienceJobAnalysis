import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

class Preprocessor:
    '''
    Defines a Preprocessor Class that defines the methods that preprocess the dataframes
    '''
    def __init__(self):
        self.is_fit = False

    def fit_preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        self.fit(df)
        df = self.preprocess(df)
        return df

    def fit(self, df: pd.DataFrame) -> None:
        self.iso_cc = Preprocessor.get_iso_codes()
        self.is_fit = True
    
    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fit:
            raise Exception("Preprocessor Needs to be Fit!")

        df = Preprocessor.map_country_codes_to_names(df, self.iso_cc)
        df = Preprocessor.convert_remote_ratio(df)
        df = Preprocessor.clean_salaries(df)
        return df

    '''
    FITTING FUNCTIONS
    '''

    @staticmethod
    def get_iso_codes() -> pd.DataFrame:
        '''
        Gets the ISO Country Codes

        Used in Fit only
        '''
        r = requests.get('https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes').text
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.findAll('table', class_ = 'wikitable sortable')
        iso_cc_df = pd.read_html(str(table[0]), header=None)[0]
        iso_cc_df = iso_cc_df.T.reset_index().drop(columns=['level_0']).iloc[[0, 3]].T.reset_index(drop=True).rename(columns={0: "Country Name", 3: "Code"}).iloc[1:, :]
        iso_cc_df.loc[1, :]['Code'] = "AF"
        iso_cc_df.dropna(inplace=True)
        to_drop = iso_cc_df[iso_cc_df['Code'].str.contains("See")].index
        iso_cc_df.drop(to_drop, inplace=True)
        iso_cc_df = iso_cc_df.reset_index(drop=True)
        return iso_cc_df
    
    '''
    PREPROCESS FUNCTIONS
    '''
    @staticmethod
    def map_country_codes_to_names(df: pd.DataFrame, cc_df: pd.DataFrame) -> pd.DataFrame:
        '''
        Map the ISO Country Codes to the df
        '''
        df = df.merge(cc_df, how='left', left_on='company_location', right_on='Code')
        df = df.merge(cc_df, how='left', left_on='employee_residence', right_on='Code')
        df.drop(columns=['Code_x', 'Code_y'], inplace=True)
        return df

    @staticmethod
    def convert_remote_ratio(df: pd.DataFrame) -> pd.DataFrame:
        df['remote_ratio'] = df['remote_ratio'] // 50
        remote_map = {
            0: "On-Site",
            1: "Hybrid",
            2: "Remote"
        }
        df['remote_ratio'] = df['remote_ratio'].map(remote_map)
        df = df.rename({'remote_ratio': 'work_type'})
        return df

    @staticmethod
    def clean_salaries(df: pd.DataFrame) -> pd.DataFrame:
        df = df.drop(columns=['salary', 'salary_currency'])
        return df