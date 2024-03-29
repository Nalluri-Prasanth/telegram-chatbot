from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup",):
        return "Hey ! sql learner"
    if user_message in ("Who are you","Who are you?",):
        return "I am sql learner bot"
    if user_message in ("time","time?",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y","%H:%M:%S")
        
        return str(date_time)

    return "type in correctly"      