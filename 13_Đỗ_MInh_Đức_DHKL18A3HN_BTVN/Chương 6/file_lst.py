import pandas as pd
import time

files = ['sales_feb.csv', 'sales_mar.csv', 'sales_apr.csv']

def read_files():
    start_time = time.time()
    
    for file in files:
        df = pd.read_csv(file)
        print(f"Đã đọc xong {file} với {len(df)} dòng.")
    
    end_time = time.time()
    print(f"Tổng thời gian đọc file: {end_time - start_time:.2f} giây")

read_files()
