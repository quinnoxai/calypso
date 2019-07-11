import random
def get_middle_response(sentence,received_dict):
    print("Here in get response")
    if "response_complete" in received_dict and received_dict["response_complete"] =="no":
        print("In if of get_response")
        return get_phase_response(sentence,received_dict)
    else:
        print("In else of get_response")
        return assign_response(sentence)



def assign_response(sentence):
    global yes,no
    yes = {"response":"Yes, all your reports are available.","response_complete":"yes","phase":"1"}
    no = {"response":"No, the Equity risk file was not generated.Should I send out an email to the support team?","response_complete":"no","phase":"1"}
    randomoutput = [yes,no]
    word = sentence
    print("Line No 5 in middle_office",word)
    new_word = word.find('reports')
    if new_word != -1:
        global random_value
        random_value = random.choice(randomoutput)
        print("Line No 7",random_value)
    return random_value



def get_phase_response(sentence,received_dict):
    if received_dict["phase"] == "1" and sentence == 'yes':
        response={"response":"An email has been sent out to support@suntrust.com"}
    return response
