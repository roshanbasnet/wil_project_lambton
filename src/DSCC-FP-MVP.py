import yfinance as yf

from filehandler.filehandler import Filehandler


class CollectData:

    def __init__(self, ticker, start_date='2021-01-01', end_date='2021-12-31', interval='1d'):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

    def fetch_data(self):
        """
          Function to fetch data using Yahoo Finance and save it to csv fie
        """
        data = yf.download(self.ticker, self.start_date,
                           self.end_date, self.interval, group_by='ticker')
        data['key_word'] = self.ticker

        # save the return data into csv file
        fh = Filehandler(path='data', filename='fetched_data.csv')
        fh.write_to_csv(data)

        print("Data Fetch completed")

        return None


# Calling function
gather_data = CollectData('AAPL', start_date='2021-01-01',
                          end_date='2021-12-31', interval='1d')

# Fetch data and save to csv file
gather_data.fetch_data()
