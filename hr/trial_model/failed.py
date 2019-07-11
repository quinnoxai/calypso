import pandas as pd
def get_failed_task(sentence,status_response_check):
    path = './././hr/trial_model/STR.xlsx'
    dataf = pd.read_excel(path)
    #print(dataf)
    columns=dataf.columns
    column_1=dataf['Status']
    #print(column_1)
    word = sentence
    loc = (word.find('failed'))
    if (loc < 0):
        stored_word = "Unsuccess"
    else:
        stored_word = "failed"
    #print(stored_word)

    fail= dataf.loc[dataf.Status == stored_word]
    #print(fail)
    new_fail=fail.head(5)
    failed_id =((new_fail)['Task ID'])
    #print(failed)
    failed_name =((new_fail)['External Ref.'])
    failed_exe_df = ((new_fail)['Execution Time'].astype(str))
    failed_erroe_df = ((new_fail)['Error Count'])
    failed_df = pd.concat([failed_id,failed_name,failed_exe_df,failed_erroe_df],axis =1)
    if status_response_check == 'failed_tasks':
        return failed_df
    else:
        return 'No data found'
    return 'No data found'

