import re
import pandas as pd
def get_status(sentence,status_response_check):

	path = './././hr/trial_model/STR.xlsx'
	df = pd.read_excel(path)
	col=df.columns
	col1=df['Status']
	col2=df['Task ID']

	question = sentence
	print(question)
	print(type(question))
	num = int(re.search(r'\d+', question).group())
	print(num)

	status = df[df['Task ID'] == num]['Status']
	task_id = df[df['Task ID'] == num]['Task ID']
	task_name = df[df['Task ID'] == num]['External Ref.']
	task_exe = (df[df['Task ID'] == num]['Execution Time'].astype(str))
	task_err = df[df['Task ID'] == num]['Error Count']
	status_id_df = pd.concat([status,task_id,task_name,task_exe,task_err],axis =1)
	tasktype = df[df['Task ID'] == num]['Task Type']
	parent = str(df[df['Task ID'] == num]['Parent Task'].iloc[0])
	Valuation = str(df[df['Task ID'] == num]['Valuation Time'].iloc[0])
	Duration = str(df[df['Task ID'] == num]['Duration (sec)'].iloc[0])

	if status_response_check == 'Task_status':
		return status_id_df
	elif status_response_check == 'Task_type':
		return tasktype
	elif status_response_check == 'Task_parent':
		return parent
	elif status_response_check == 'Task_valuation':
		return Valuation
	else:
		return 'No data found'
	return 'No data found'
