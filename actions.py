# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="أعتَذِرُ مِنْكَ لِازِلتُ أتَعَلم لأُجِيبك عَلى جَميعِ استفسراتكْ")
#         dispatcher.utter_message(text="الرجاء الإنتظار")
#         dispatcher.utter_message(text="بِمَاذَا يُمْكِنُني مُساعَدَتُكَ اَيْضًا ")
#         return []

class ActionRequests(Action):

    def name(self) -> Text:
        return "action_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        req=tracker.get_slot("request")
        if req == "عرض وايداع":
            dispatcher.utter_message(template = 'utter_offer-and-deposit')
        elif req == "امر على عريضة":
            dispatcher.utter_message(template = 'utter_petition-order') 
        elif req == "امر آداء":
            dispatcher.utter_message(template = 'utter_writ-of-payment')
        elif req == "الحجز التحفظي":
            dispatcher.utter_message(template = 'utter_sequestration') 
        elif req == "التنفيذ":
            dispatcher.utter_message(template = 'utter_execution-proceeding')     
        else:
            dispatcher.utter_message(text="لم افهم")
        return []    

class ActionClaim(Action):

    def name(self) -> Text:
        return "action_claim"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=""    
        claim=tracker.get_slot("claim")
        if claim == "النزاع":
            dispatcher.utter_message(template = "utter_dispute_claim")
        elif claim == "الابتدائية":
            dispatcher.utter_message(template = "utter_first-instance")
        elif claim == "الاستئنافية":
            dispatcher.utter_message(template = 'utter_appeal')
        elif claim == "تفسير حكم":
            dispatcher.utter_message(template = 'utter_judgment-interpretation')
        elif claim == "إغفال في الحكم":
            dispatcher.utter_message(template = 'utter_omission-in-judgment')
        elif claim == "التظلم":
            dispatcher.utter_message(template = 'utter_grievance')
        elif claim == "التماس إعادة النظر":
            dispatcher.utter_message(template = 'utter_writ-of-certiorari')           
        else:
            dispatcher.utter_message(text="لم افهم")

        return []
               