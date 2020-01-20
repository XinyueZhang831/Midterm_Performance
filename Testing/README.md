# Testing Code

### Input

- exam_path

  Give the grade csv file dir

- out_path

  Give the output dir, where you want to save the result

- exam_name

  Name of the exam

- point_range=20
  
  Grade range (e.g. 0-59, 60-79 ...,  default is 20)

- total_points=100

  Maximum points in this exam (default is 100)

- base_point=60

  The first box you want to show (e.g by default, the first box is 0-59)

- col=7

  Which number of column is the exam grade column (default is 7, when download grade file from Blackboard, choose a specific exam column)
  
  ### Output
  
  ```bash
  # give input
  mid = Midterm(exam_path, out_path,exam_name,total_points=100, base_point=60, point_range=20)
  # modify inpute file so it can be use for other function
  df, x = mid.general()
  # save histogram to output dir
  mid.his(df,x)
  # save line graph to output dir
  mid.line()
  # print mean, median, standerd deviation
  mid.mean()
  mid.median()
  mid.std()
  ```
  
  ### Example output
  
  ![Output](/Testing/example.png)
  
  ![Histogram](/Testing/Midterm2_histgram.png)
  
  ![Line Graph](/Testing/Midterm2_line.png)
  
