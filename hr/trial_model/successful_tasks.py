import pandas as pd
def get_successful_task(sentence,status_response_check):
    path = './././hr/trial_model/STR.xlsx'
    dataf = pd.read_excel(path)
    #print(dataf)
    columns=dataf.columns
    column_1=dataf['Status']
    #print(column_1)
    word = sentence

# Substring is searched in 'eks for geeks'
    loc = (word.find('successful task'))
    if (loc < 0):
        stored_word = "Unsuccess"
    else:
        stored_word = "success"
    #print(stored_word)

    succ= dataf.loc[dataf.Status == stored_word]
    print("Here1",succ)
    new_succ=succ.head(5)
    status_id_df =((new_succ)['Task ID'])
    print(status_id_df)
    status_name_df = ((new_succ)['External Ref.'])
    print(status_name_df)
    status_exe_df = ((new_succ)['Execution Time'].astype(str))
    print(status_exe_df)
    status_erroe_df = ((new_succ)['Error Count'])
    status_user_df = ((new_succ)['User'])
    data_df = pd.concat([status_id_df,status_name_df,status_exe_df,status_erroe_df],axis =1)
    print(data_df)
    if status_response_check == 'successful_tasks':
        return data_df
    else:
        return 'No data found'
    return 'No data found'

