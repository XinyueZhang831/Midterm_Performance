import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def list_pointrange(bin, total, base):
    list_range = []
    if base !=0:
        list_range.append((0,base))
    while base<=total:
        tmp = base+bin-1
        if tmp >=total:
            tmp=total
        list_range.append((base,tmp))
        base = tmp+1
    return list_range


def modify_colname(df_path, exam_col, exam_name):
    df=pd.read_csv(df_path)
    df = df.fillna(0)
    df_col = list(df.columns)[exam_col - 1]
    df = df.rename(columns={df_col: exam_name})
    df_col = exam_name
    return df, df_col


class Midterm():

    def __init__(self, exam_path,out_path, exam_name, point_range=20, total_points=100, base_point=60, col=7):
        self.ep = exam_path
        self.col = col
        self.op = out_path
        self.tp = total_points
        self.bp = base_point
        self.pr = point_range
        self.en = exam_name

    def general(self):
        df, df_col = modify_colname(self.ep, self.col, self.en)
        point_range = list_pointrange(self.pr, self.tp, self.bp)
        x_axis = []
        for each in point_range:
            df.loc[(df[df_col] <= each[1]) & (df[df_col] >= each[0]), 'Grade Range'] = str(each[0])+' - '+str(each[1])
            x_axis.append(str(each[0])+' - '+str(each[1]))
        return df, x_axis

    def his(self, df, x_axis):
        df = df.fillna(0)
        plt.figure(figsize=(15, 8))
        sns_plot = sns.countplot(x='Grade Range', data=df,
                                 order=x_axis,
                                 color='xkcd:azure')
        fig = sns_plot.get_figure()
        fig.savefig(self.op+'/'+self.en+'_'+'histgram.png',
                    inplace=True)
        print('histgram graph has been save to ' + self.op)

    def line(self):
        df, df_col = modify_colname(self.ep, self.col, self.en)
        df = df.sort_values(by=[df_col])
        df = df.reset_index(drop=True)
        line = df.reset_index().plot(x='index', y=df_col, marker='o', figsize=(14, 8))
        fig1 = line.get_figure()
        fig1.savefig(self.op+'/'+self.en+'_'+'line.png',
                     inplace=True)
        print('line graph has been save to '+self.op)

    def mean(self):
        df, df_col = modify_colname(self.ep, self.col, self.en)
        print('mean of this class:  ', round(df[df_col].mean(),2))

    def median(self):
        df, df_col = modify_colname(self.ep, self.col, self.en)
        print('median of this class:  ', round(df[df_col].median(), 2))

    def std(self):
        df, df_col = modify_colname(self.ep, self.col, self.en)
        print('std of this class:  ', round(df[df_col].std(), 2))




