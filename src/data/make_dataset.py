# -*- coding: utf-8 -*-
import logging
import numpy as np
import pandas as pd

log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)


class PakWheelsETL:
    def __init__(self):
        self._logger = logging.getLogger('PakWheels ETL')

    def ETL(self, input_filepath):
        """
            Following piece of code transforms data into use able format for the exploration phase. It involves
            data cleaning,feature engineering/extraction etc. The new dataframe is saved as csv file in root
            directory.

            :param input_filepath: directory path where source files exist
            :return: none

        """

        """
            Following piece of code extracts data from raw data file. This is extraction part of ETL pipeline.
        """
        self._logger.info('Starting ETL process....')
        self._logger.info('Extracting raw data....')
        df=pd.read_csv('data/raw/pakwheels.csv')

        """
            Following piece of code does data transformation in such a way that it is ready for exploratory data analysis.
            Duplicates are removed, null values are removed, new features are created and more.
        """
        self._logger.info('Starting transformation process...')
        self._logger.info('Dropping unnecessary columns....')
        df.drop(['Unnamed: 0', 'ad_url', 'ad_last_updated'], inplace=True, axis=1)
        self._logger.info('Dropping Duplicates.....')
        df.drop_duplicates(inplace=True)
        self._logger.info('Doing preprocessing....')
        self._logger.info('Please wait....')
        df['manufacturer'] = df['title'].str.split(' ', expand=True)[0]
        df['car_name'] = df['manufacturer'] + ' ' + df['title'].str.split(' ', expand=True)[1]
        df['city/state'] = np.where(df['location'].str.contains(','), df.location.str.split(',', expand=True)[1],df.location)
        df['currency'] = df['price'].str.split(' ', expand=True)[0]
        df['amount'] = df['price'].str.split(' ', expand=True)[1]
        df['suffix'] = df['price'].str.split(' ', expand=True)[2]
        df['amount'].fillna(0, inplace=True)
        df['amount'] = df['amount'].str.replace('for', '0')
        df['amount'] = df.amount.str.replace(',', '')
        df['amount'] = df['amount'].astype('float')
        df=df[df['suffix'].notna()]
        df['suffix'] = df['suffix'].str.replace('lacs', '100000')
        df['suffix'] = df['suffix'].str.replace('crore', '10000000')
        df['suffix'] = df['suffix'].str.replace('price', '0')
        df['suffix'] = np.where(df['suffix'].isnull() & df['amount'] > 0, "1", df['suffix'])
        df['suffix'] = df['suffix'].astype('int64')
        df['new_price'] = df['amount'] * df['suffix']
        df['mileage_unit'] = df['mileage'].str.split(' ', expand=True)[1]
        df['mileage'] = df['mileage'].str.replace(',', '')
        df['mileage'] = df['mileage'].str.replace('km', '')
        df['mileage'] = df['mileage'].astype('int32')
        df['engine_capacity_suffix'] = df['engine_capacity'].str.split(' ', expand=True)[1]
        df['ev/non-ev'] = np.where(df['engine_capacity_suffix'] == 'kWh', 'electric', 'non-electric')
        df['car_features_clean'] = df['car_features'].str.replace('\n', ',')
        df['car_features_clean'] = np.where(df['car_features_clean'].isnull() == True, 'None', df['car_features_clean'])
        features_list = []
        for i in df['car_features_clean'].str.split(','):
            for j in i:
                features_list.append(j)
        features_unique = set(features_list)
        features_unique = list(features_unique)
        for i in features_unique:
            df[i] = np.where(df['car_features_clean'].str.contains(f'{i}') == True, 1, 0)
        delete_cols = ['location', 'price', 'car_features', 'description', 'currency', 'amount', 'suffix',
                       'mileage_unit', 'engine_capacity_suffix', 'car_features_clean', 'None']
        df.drop(delete_cols, axis=1, inplace=True)

        self._logger.info('Loading process starts...')
        """
            This piece of code converts dataframe to a csv file and saves in root directory of this project.
            I have saved it in data/processed folder.
        """
        df.to_csv('clean_data.csv')




if __name__ == '__main__':
    pass
