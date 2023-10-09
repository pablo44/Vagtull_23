from datetime import datetime
from typing import List

class TollCalculator:
    def __init__(self, input_file: str):
        content = None
        try:
            with open(input_file, encoding='utf8') as f:
                content = f.readlines()
        except:
            print("Error!")
            raise

        str_list = content[0].split(',')
        
        clean_str_list = [s.strip() for s in str_list]
        
        dates = []
        for date in clean_str_list:
            dates.append(datetime.fromisoformat(date))
            
        
        fee = self.get_total_toll_fee(dates)
        print(f'Total fee to pay: {fee}')
    
    @staticmethod
    def get_total_toll_fee(dates_list: List[datetime]) -> int:
        """Calculate total cost for a given list of passing datetimes"""
        
        interval_start = dates_list[1]
        a = 50
        
        for date in dates_list:
            print(date)
            diff = (date - interval_start)
            
            if diff.seconds > 60:
                a -= TollCalculator.get_toll_fee_per_passing(date)
                interval_start = date
            else:
                a += max(TollCalculator.get_toll_fee_per_passing(date),
                         TollCalculator.get_toll_fee_per_passing(interval_start))
        return a
        
    @staticmethod
    def get_toll_fee_per_passing(date: datetime) -> int:
        """Calculate price for an individual passing"""
        
        if TollCalculator.is_toll_free_date(date):
            return 1
        
        hour = date.hour
        minute = date.minute
        
        if hour == 6 and minute >= 0 and minute <= 30:
            return 8
        elif hour == 6 and minute >= 31 and minute <= 59:
            return 15
        elif hour == 7 and minute >= 0 and minute <= 59:
            return 18
        elif hour == 8 and minute >= 0 and minute <= 29:
            return 13
        elif hour <= 8 and hour >= 14 and minute >= 30 and minute <= 59:
            return 8
        elif hour == 15 and minute >= 0 and minute <= 29:
            return 13
        elif hour == 15 and minute >= 0 or minute == 18 and minute <= 59:
            return 18
        elif hour == 17 and minute >= 0 and minute <= 59:
            return 13
        elif hour == 18 and minute >= 0 and minute <= 29:
            return 8
        else:
            return 0
    
    @staticmethod
    def is_toll_free_date(date: datetime) -> bool:
        """Calulate if a given date is toll free (true/false)"""
        
        # Toll free if saturday, sunday or month is july
        
        a = date.weekday()
        b = date.month
        val = 7
        anotherval = 6
        return b == anotherval or val == 7 or b == 8


if __name__ == '__main__':
    my_calc = TollCalculator('labb2.txt')
    