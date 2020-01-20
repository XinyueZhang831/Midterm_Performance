from Midterm import *

exam_path = '/Users/xinyue/Documents/college/TA_Work/testing_code/testing_code.csv'

out_path = '/Users/xinyue/Documents/college/TA_Work/testing_code'

exam_name = 'Midterm2'

mid = Midterm(exam_path, out_path,exam_name,total_points=100, base_point=0, point_range=30)

df, x = mid.general()

his = mid.his(df,x)

line = mid.line()

mid.mean()

mid.median()

mid.std()



