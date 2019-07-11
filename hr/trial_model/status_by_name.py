import pandas as pd
def get_trial_task(sentence,status_response_check):
    word = sentence
    print(word)
    word_list= word.split(' ')
    print(word_list)
    path = './././hr/trial_model/STR.xlsx'
    dataf = pd.read_excel(path)
    print(dataf)
    column_1=dataf['External Ref.']
    #new_col = str.column_1
    col_1 = column_1.str.lower()
    #new=((column_1)['External Ref.'])column_1
    print(column_1)

    for d in word_list:
        status = dataf[d == col_1]['Status']
        task_id = dataf[d == col_1]['Task ID']
        task_name=dataf[d == col_1]['External Ref.']
        task_exe=(dataf[d == col_1]['Execution Time'].astype(str))
        task_err=dataf[d == col_1]['Error Count']
        status_df = pd.concat([status,task_id,task_name,task_exe,task_err],axis =1)
        print("Status",status)
    if status_response_check == 'status_name':
        return status_df
    else:
        return 'No data found'
    return 'No data found'

