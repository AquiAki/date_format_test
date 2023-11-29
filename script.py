from datetime import datetime
import re

def format_date(input_date):
    # 年、月、日を抽出
    match = re.search(r'(\d{1,4})[年|R|/|.](\d{1,2})[月|/|.](\d{1,2})[日|/|.]*', input_date)
    
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        # 年号がある場合は変換
        if 'R' in input_date or '令和' in input_date:
            #令和元年
            if match.group(1) == 1:
              year += 2019
            else:
                year += 2018
        elif 'H' in input_date or '平成' in input_date:
            #平成元年
            if match.group(1) == 1:
              year += 1989
            else:
              year += 1988
        elif 'S' in input_date or '昭和' in input_date:
            #昭和元年
            if match.group(1) == 1:
              year += 1926
            else:
               year += 1925
        elif 'T' in input_date or '大正' in input_date:
            #大正元年
            if match.group(1) == 1:
              year += 1912
            else:
               year += 1911
        else:
            year = year
            
        formatted_date = datetime(year, month, day).strftime('%Y-%m-%d')
        return formatted_date
    elif len(input_date) == 8:
        year = int(input_date[:4])
        month = int(input_date[4:6])
        day = int(input_date[6:8])
        formatted_date = datetime(year, month, day).strftime('%Y-%m-%d')
        return formatted_date
    else:
        return None