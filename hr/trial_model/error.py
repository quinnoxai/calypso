import pandas as pd
def get_error_task(sentence,status_response_check):
    path = './././hr/trial_model/STR.xlsx'
    dataf = pd.read_excel(path)
    #print(dataf)
    columns=dataf.columns
    column_1=dataf['Status']
    #print(column_1)
    word = sentence
    #print(word)
# Substring is searched in 'eks for geeks'
    loc = (word.find('errors'))
    if (loc < 0):
        stored_word = "Unsuccess"
    else:
        stored_word = "finished with errors"
    #print(stored_word)

    err= dataf.loc[dataf.Status == stored_word]
    #print(err)
    new_err=err.head(5)
    error_id =((new_err)['Task ID'])
    error_name =((new_err)['External Ref.'])
    error_exe_df = ((new_err)['Execution Time'].astype(str))
    error_count_df = ((new_err)['Error Count'])
    error_df = pd.concat([error_id,error_name,error_exe_df,error_count_df],axis =1)
    #new_error_df = [error_df]
    #print(new_error_df)
    if status_response_check == 'finish_with_error_tasks':
        return error_df
    else:
        return 'No data found'
    return 'No data found'

