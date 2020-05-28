import pandas as pd

def getDF_C():
    df_C = pd.read_csv("cse 163 datasets/C/state_csv.csv")
    df_C.columns = ["0", '1', '2', '3', '4', '5', '6', '7', '8']
    df_C = df_C.loc[10:64, ['0', '5']]
    df_C = df_C.dropna()
    df_C.columns = ['State', '2017-2018 Percentage Poverty']
    return df_C

def getDF_D():
    df = pd.read_csv("cse 163 datasets/D/tableA1_csv.csv")
    df = df.loc[16:20, ['Table with row headers in column A and column headers in row 4 through 6.', 'Unnamed: 1',
                        'Unnamed: 2', 'Unnamed: 4', 'Unnamed: 5']]
    df.columns = ['Race', '2017 Number (thousands)', '2017 Median Income', '2018 Number (thousands)',
                  '2018 Median Income']
    return df

def main():
    df = pd.read_csv("cse 163 datasets/D/tableA1_csv.csv")
    df = df.loc[16:20, ['Table with row headers in column A and column headers in row 4 through 6.', 'Unnamed: 1',
                        'Unnamed: 2', 'Unnamed: 4', 'Unnamed: 5']]
    df.columns = ['Race', '2017 Number (thousands)', '2017 Median Income', '2018 Number (thousands)',
                  '2018 Median Income']
    return df


if __name__ == '__main__':
    main()
