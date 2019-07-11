import pandas as pd
def get_nottrigger_task(sentence,status_response_check):
    path = './././hr/trial_model/STR.xlsx'
    dataf = pd.read_excel(path)
    print(dataf)
    columns=dataf.columns
    column_1=dataf['Status']
    #print(column_1)
    word = sentence
    loc = (word.find('trigger'))
    if (loc < 0):
        stored_word = "Unsuccess"
    else:
        stored_word = "not triggered"
    print(stored_word)

    trr= dataf.loc[dataf.Status == stored_word]
    print(trr)
    not_trr=trr.head(5)
    not_triggered_id =((not_trr)['Task ID'])
    not_triggered_name =((not_trr)['External Ref.'].astype(str))
    status_exe_df = ((not_trr)['Execution Time'])
    print(status_exe_df)
    status_error_df = ((not_trr)['Error Count'])
    #status_user_df = ((new_succ)['User'])
    data_df = pd.concat([not_triggered_id,not_triggered_name,status_exe_df,status_error_df],axis =1)    #print(not_triggered)
    if status_response_check == 'untriggered_tasks':
        return data_df
    else:
        return 'No data found'
    return 'No data found'

