import pandas as pd
def get_trial_task():
    word = "Show me the status of BALANCE_1_CHAIN"
    print(word)
    word_list= word.split(' ')
    print(word_list)
    path = 'D:/final_calypso_bot_bk/hr/trial_model/STR.xlsx'
    dataf = pd.read_excel(path)
    print(dataf)
    column_1=dataf['External Ref.']
    #new=((column_1)['External Ref.'])column_1
    print(column_1)

    for d in word_list:
        status = dataf[d == column_1]['Status']
        print("Status",status)
get_trial_task()

