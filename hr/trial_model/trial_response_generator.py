import json
import random
import requests
from ..quick_menu import find_quick_menu
import os
import json
import pandas as pd
from hr.trial_model import intent_classification as ic
from ..check_if_empty import is_empty
from .status_indicator import get_status
from .successful_tasks import get_successful_task
from .failed import  get_failed_task
from .error import get_error_task
from .status_by_name import get_trial_task
from .middle_office_response import get_middle_response
from .not_trigger import get_nottrigger_task
from hrhelpdesk.settings import BASE_DIR

data_out_total = {"data": [{"name": "add user"},{"name": "status report"},{"name":"Task_parent"},{"name":"Task type"}, {"name": "mirror existing user"}, {"name": "group access permission"},
                           {"name": "locked user"}, {"name": "reset password"}, {"name": "existing trades"},
                           {"name": "pricing sheet"}, {"name": "pricing grid"}, {"name": "risk config"}, {"name": "calypso workstation"}, {"name": "ob-demand analysis"}, {"name": "loading particular trade"},
                           {"name": "loading particular message"}, {"name": "loading particular posting"}, {"name": "loading particular transfer"}, {"name": "data authorization"}, {"name": "booked product type"}, {"name": "booked trades on particular date"},
                           {"name": "booked defined"}, {"name": "trading book"}, {"name": "accounting book link"}, {"name": "accounting event"}, {"name": "counterparty trade"}, {"name": "accounting rule"},
                           {"name": "static data filter"}, {"name": "trade filter"}, {"name": "filterset"}, {"name": "legal entity"},{"name": "message set-up"}, {"name": "message sender"},{"name": "settlement delivery instruction"},{"name": "workflow"},{"name": "domain values"},
                           {"name": "scheduled task"},{"name": "scheduled task window"},{"name": "cost associated with each user"},{"name":"new user permission"},{"name": "raise support ticket"},{"name": "request for enhancement"},{"name": "technology used for calypso"},{"name": "add trading book"},{"name": "market book"},{"name": "software requirements while installing Calypso"},{"name": "jnlp file"}]}
dats = ["I can also help you with the following", "How else can I help you?", "You can enquire about the following too",
        "I hope this was what you need, I can tell you more about the following"]


def classify_intent(sentence):
    intent_received = ic.classify(sentence)
    return intent_received


def get_response(sentence, received_dict, master_intent):
    print("#####################",received_dict)
    if "response_complete" in received_dict and received_dict["response_complete"]=="no":
        model_intent=["my_reports"]
    else:
        model_intent = classify_intent(sentence)

    dict_return={}
    print("Line no 43 in trial response",model_intent)
    with open(os.path.join(BASE_DIR, r'hr/trial_model/trial.json'), encoding="utf-8")as json_data:
        intents = json.load(json_data)

    for i in intents["intents"]:
        if i["intent"] == model_intent[0]:
            # response = "<p>"+"At Quinnox, we take good care of our employees and cover them from very first day."+"<br/>"+"To know maore about mediclaim please download the below pdf or if you have any specific query please let me know."+"<br/>" + i["response"] + "</p> <br/>" + random.choice(dats)
            status_response_check =  i["response"]
            if status_response_check == 'Task_status':
                status_response=get_status(sentence,status_response_check)
                response = status_response
                status_list=response.values.tolist()
                print("list",status_list)
                data={"data":[{'Status':a,'Task ID':b,'External Ref':c,'Execution Time':d,'Error Count':e}for a,b,c,d,e in status_list]}
                response = pd.DataFrame(response)
                print("response below")
                print(response)
                response = response.reset_index()
                response.drop('index',axis =1,inplace = True)
                print(response.columns)
                print(response)
                response = response['Status'].iloc[0]
                print(response)
                print("RESPONSE TYPE",type(response))
                response_new=''.join(e for e in response if e.isalnum())
                dict_return["new_value"] = response_new
                dict_return["response"] = data
                dict_return["output"] = "Status"
                print('statust check',status_response_check)
            elif status_response_check == 'Task_type':
                status_response=get_status(sentence,status_response_check)
                response = "<p>" + "Task Type is:"+"<br/>"+status_response+ "</p>" + "<p>Would you like to know more?</p>"
                dict_return["response"] = response
                print('statust check',status_response_check)
            elif status_response_check == 'Task_parent':
                status_response=get_status(sentence,status_response_check)
                response = "<p>" + "Task parent is:"+"<br/>"+status_response+ "</p>" + "<p>Would you like to know more?</p>"
                dict_return["response"] = response
                print('statust check',status_response_check)
            elif status_response_check == 'status_name':
                status_response=get_trial_task(sentence,status_response_check)
                response = status_response
                status_list=response.values.tolist()
                print("list",status_list)
                data={"data":[{'Status':a,'Task ID':b,'External Ref':c,'Execution Time':d,'Error Count':e}for a,b,c,d,e in status_list]}
                response = pd.DataFrame(response)
                print("response below")
                print(response)
                response = response.reset_index()
                response.drop('index',axis =1,inplace = True)
                print(response.columns)
                print(response)
                response = response['Status'].iloc[0]
                print(response)
                print("RESPONSE TYPE",type(response))
                response_new=''.join(e for e in response if e.isalnum())
                dict_return["new_value"] = response_new
                dict_return["response"] = data
                dict_return["output"] = "Status"
                print('statust check',status_response_check)
            elif status_response_check == 'successful_tasks':
                status_response=get_successful_task(sentence,status_response_check)
                status_list=status_response.values.tolist()
                print("list",status_list)
                data={"data":[{'Task ID':a,'External Ref':b,'Execution Time':c,'Error Count':d}for a,b,c,d in status_list]}
                dict_return["data"]=data
                dict_return["response"]="Hey Sara, here are the successful tasks list you enquired for"
                dict_return["output"]="table"
            elif status_response_check == 'Task_valuation':
                status_response=get_status(sentence,status_response_check)
                response = "<p>" + "Task Valuation time is:"+"<br/>"+status_response+ "</p>" + "<p>Would you like to know more?</p>"
                dict_return["response"] = response
                print('Valuation check',status_response_check)
            elif status_response_check == 'failed_tasks':
                status_response=get_failed_task(sentence,status_response_check)
                status_list=status_response.values.tolist()
                data = {"data": [{'Task ID': a, 'External Ref': b, 'Execution Time': c, 'Error Count': d} for a, b, c, d in status_list]}
                dict_return["data"]=data
                dict_return["response"]="Hey Sara, here are the failed tasks list you enquired for"
                dict_return["output"]="table"
                dict_return["type"]="Failed Tasks"
            elif status_response_check == 'finish_with_error_tasks':
                status_response=get_error_task(sentence,status_response_check)
                status_list=status_response.values.tolist()
                data = {"data": [{'Task ID': a, 'External Ref': b, 'Execution Time': c, 'Error Count': d} for a, b, c, d in status_list]}
                dict_return["data"]=data
                dict_return["response"]="Hey Sara, here are the tasks finished with errors list you enquired for"
                dict_return["output"]="table"
            elif status_response_check == 'untriggered_tasks':
                status_response=get_nottrigger_task(sentence,status_response_check)
                status_list=status_response.values.tolist()
                data={"data":[{'Task ID':a,'External Ref':b,'Execution Time':c,'Error Count':d}for a,b,c,d in status_list]}
                dict_return["data"]=data
                dict_return["response"]="Hey Sara, here are the untriggreded tasks list you enquired for"
                dict_return["output"]="table"
            elif status_response_check == 'about_user_guide':
                dict_return["response"] = "Here's your User Guide SOP(Standard Operating Procedure Document)"
                dict_return["output"] = "pdf"
                dict_return["data"]={"data": [{"type_data": "img","data_link": "/static/images/UserGuide.docx","name":"SOP"}]}
            elif status_response_check == 'about_book_creation':
                dict_return["response"] = "Here's your Book Creation SOP(Standard Operating Procedure Document)"
                dict_return["output"] = "pdf"
                dict_return["data"]={"data": [{"type_data": "img","data_link": "/static/images/bookcreation.docx","name":"SOP"}]}
            elif status_response_check == 'my_reports':
                status_response = get_middle_response(sentence,received_dict)
                dict_return= status_response

            else:
                response = "<p>" + i["response"] + "</p>" + "<p>Would you like to know more?</p>"
                dict_return["response"] = response
            # dict_return["response"] = response


    return dict_return
