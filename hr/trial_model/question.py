def get_nottrigger_task(sentence,status_response_check):
    word = 'No the Equity risk file was not generated.Should I send out an email to the support team?'

# Substring is searched in 'eks for geeks'
    loc = (word.find('Should I send out an email to the support team?'))
    print(loc)
    if (loc < 0):
        stored_word = "Unsuccessful"
    else:
        stored_word = "Yes"
        if (stored_word is "Yes"):
            print("Email sent")
    return "Email sent"

