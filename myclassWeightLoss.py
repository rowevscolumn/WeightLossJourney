import numpy as np
import pandas as pd
import os
import sys
from datetime import datetime
from pytz import timezone, all_timezones

class WeightLoss:
    """
    Allows to trace the results of your weight loss journey. Saves it to a CSV file for use of other programs like Power BI.

    Args:
        csvfile (str='weightloss.csv'): The csv file. Can use the default file, or another if you want to make multiple files.
        weightloss (str='US/Eastern'); Timezone from pytz which is your local time.

    """
    def __init__(self, csvfile: str = 'weightloss.csv', timezone:str = 'US/Eastern') -> None:
        self.csvfile: str = csvfile
        self.timezone: str = timezone
        self.df = pd.DataFrame(columns=["date", "weight"])
        self.df = self.df.set_index(['date'])
        pass

    def __str__(self) -> str:
        """
        Returns the DataFrame in string format to view.
        """
        return self.df.to_string()
    
    def printdf(self) -> pd.DataFrame:
        """
        Returns the dataframe so you can use Dataframe functions

        Returns:
            pd.DataFrame

        """
        return self.df

    def opencsvfile(self)-> bool:
        """
        Opens the csv file into a dataframe. Checks first to see if the file name exists first.
        """
        if os.path.isfile(self.csvfile):
            self.df = pd.read_csv(self.csvfile)
            self.df = self.df.set_index(['date'])
        else:
            print("File name missing, will leave blank DataFrame as is.")
        return True   
    
    def addnewweight(self, newweight: float)-> bool:
        """
        Will take the new weight number, and add a new record to the csv file. 

        Args:
            newweight (float): Your new weight
        """
        newdate = datetime.now().astimezone(timezone(self.timezone)).isoformat()
        self.df.loc[newdate] = [newweight]
        return True
    pass # End Class Weightloss

    def savecsvfile(self)-> bool:
        """
        Saves the dataframe into a csv file
        """
        self.df.to_csv(self.csvfile)
        return True
    
    def lastknownweight(self)-> float:
        """
        Returns the last known weight, so that it's the default number shown in the text field in the notebook.

        Returns:
            float: Last number in the csv file

        """
        if self.df.shape[0] <= 0:
            return 0
        return self.df.at[self.df.index.max(), 'weight']
    
    def updateTimeZone(self, newtimezone:str) -> bool:
        """
        Description of updateTimeZone

        Args:
            newtimezone (str): The new time zone. Will be validated in the Pytz library.
        """
        if newtimezone in all_timezones:
            self.timezone = newtimezone
        else:
            raise ValueError('Invalid timezone from Pytz! Double check the text.')
        return True

    pass # END Class Weightloss
