import csv
import matplotlib.pyplot as plt
from time import time as tim
import pandas as pd
from forInvestigation import write_to_csv_file as csvwriter
import forInvestigation
import numpy as np


def csv_reader():
    data = pd.read_csv("C:/Users/ducat/Documents/Portfolio/Python_Projects/generated_numbers.csv")
    print('There are no Zeros or Null in:', '\n', (data != 0).all(bool_only=False))
    plt.figure(facecolor='grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    plt.title('Random_Numbers Scatter Plot', color="red")
    plt.xlabel('Time', fontweight='bold', color='white')
    plt.ylabel('Random_Numbers', fontweight='bold', color='blue')
    plt.grid(True)
    plt.plot(data['Random_Numbers'])
    choice = (input('do you wish to repair a column?')).lower()
    if choice == 'yes' or choice == 'y' or choice == 1:
        n = input('\nWhich column do you wish to check for zeros?')
        # '\nUse commas to separate with NO SPACES!')
        n = n.split(',')
        print(data)
        data2 = data[n].mask(data[n] == 0).fillna(data[n].mean())  # <- handles nulls as well
        # data2 = data[n].rolling(3, 1).apply(lambda x: np.nanmean(x))
        print('The new mean: ', data[n].mask(data[n] == 0).fillna(data[n].mean()), 'There are no Zeros or Null in:',
              '\n',  # data2[n].rolling(3, 1).apply(lambda x: np.nanmean(x))
              (data2[n] != 0).all(bool_only=False))
        print(data2)
        plt.plot(data2)
        plt.ylabel(n)
        plt.show()
        data2.to_csv("generated_numbers2.csv", encoding='utf-8', index=False)
        print('file written')
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
        # https://realpython.com/pandas-read-write-files/#using-the-pandas-read_csv-and-to_csv-functions


def csv_reader_rolling_avg():
    data = pd.read_csv("C:/Users/ducat/Documents/Portfolio/Python_Projects/generated_numbers.csv")
    print('There are no Zeros or Null in:', '\n', (data != 0).all(bool_only=False))
    plt.figure(facecolor='grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    plt.title('Random_Numbers Scatter Plot', color="red")
    plt.xlabel('Time', fontweight='bold', color='white')
    plt.ylabel('Random_Numbers', fontweight='bold', color='blue')
    plt.grid(True)
    plt.plot(data['Random_Numbers'])
    # choice = (input('do you wish to repair a column?')).lower()
    choice = 'y'
    if choice == 'yes' or choice == 'y' or choice == 1:
        # n = input('\nWhich column do you wish to check for zeros?')
        # # '\nUse commas to separate with NO SPACES!')
        # n = n.split(',')
        n = 'Random_Numbers'
        print(data)
        # data2 = data[n].mask(data[n] == 0).fillna(data[n].mean())  # <- handles nulls as well
        # data['ma'] = data[n].rolling(3, 1).apply(lambda x: np.nanmean(x))
        data['ma'] = data[n].rolling(4, 2).apply(lambda x: np.nanmean(x))
        data['final'] = np.where(data[n] > 0, data[n], data['ma'])
        # print('The new mean: ', data[n].mask(data[n] == 0).fillna(data[n].mean()), 'There are no Zeros or Null in:',
        #       '\n',  # data2[n].rolling(3, 1).apply(lambda x: np.nanmean(x))
        # (data[n] != 0).all(bool_only=False))
        data.drop('ma', axis=1, inplace=True)
        print(data)
        plt.plot(data)
        plt.ylabel(n)
        # plt.show()
        data.to_csv("generated_numbers2.csv", encoding='utf-8', index=False)
        print('file written')


def csv_reader_sqlFile():
    data = pd.read_csv(
        "C:/Users/ducat/Documents/UNCW_Grad_school/MIS 504_Database_of_Analytics/NorthWindDataBase/Orders.csv")
    # print('There are no Zeros or Null in:', '\n', (data != 0).all(bool_only=False))
    print(f'Data head: \n{data.head()}')
    print(f'DataShape: {data.shape}')
    print(f'Columns : \n{data.columns}')
    print(f'Index: \n{data.index}')
    # plt.figure(facecolor='grey')
    # ax = plt.axes()
    # ax.set_facecolor('grey')
    # plt.title('Random_Numbers Scatter Plot', color="red")
    # plt.xlabel('Time', fontweight='bold', color='white')
    # plt.ylabel('Random_Numbers', fontweight='bold', color='blue')
    # plt.grid(True)
    # plt.plot(data['Random_Numbers'])
    ## choice = (input('do you wish to repair a column?')).lower()
    # choice = 'y'
    # if choice == 'yes' or choice == 'y' or choice == 1:
    #    # n = input('\nWhich column do you wish to check for zeros?')
    #    # # '\nUse commas to separate with NO SPACES!')
    #    # n = n.split(',')
    #    n = 'Random_Numbers'
    #    print(data)
    #    # data2 = data[n].mask(data[n] == 0).fillna(data[n].mean())  # <- handles nulls as well
    #    # data['ma'] = data[n].rolling(3, 1).apply(lambda x: np.nanmean(x))
    #    data['ma'] = data[n].rolling(4, 2).apply(lambda x: np.nanmean(x))
    #    data['final'] = np.where(data[n] > 0, data[n], data['ma'])
    #    # print('The new mean: ', data[n].mask(data[n] == 0).fillna(data[n].mean()), 'There are no Zeros or Null in:',
    #    #       '\n',  # data2[n].rolling(3, 1).apply(lambda x: np.nanmean(x))
    #    # (data[n] != 0).all(bool_only=False))
    #    data.drop('ma', axis=1, inplace=True)
    #    print(data)
    #    plt.plot(data)
    #    plt.ylabel(n)
    #    #plt.show()
    #    data.to_csv("generated_numbers2.csv", encoding='utf-8', index=False)
    #    print('file written')


if __name__ == '__main__':
    start = tim()
    # csv_reader()
    # csv_reader_rolling_avg()
    csv_reader_sqlFile()
    finish1 = tim() - start
    print(f'Completed in :{finish1}')
