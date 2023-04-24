# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def text_date_to_int(text_date):
    print("text_date {}".format(text_date))
    if text_date == "hoje":
        return 0
    if text_date == "amanha":
        return 1
    if text_date == "ontem":
        return -1

    # em outro caso
    return None

def get_pre_date(text_date):
    if text_date == "hoje":
        return "É"
    if text_date == "amanha" or text_date == "amanhã":
        return "Será"
    if text_date == "ontem":
        return "Foi"

    # em outro caso
    return None

weekday_mapping = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

def weekday_to_text(weekday):
    return weekday_mapping[weekday]

class ActionQueryTime(Action):

    def name(self) -> Text:
        return "action_query_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_time = datetime.now().strftime("São %H:%M %p.")
        dispatcher.utter_message(text=current_time)

        return []
    
class ActionQueryDate(Action):
    def name(self) -> Text:
        return "action_query_date"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_date = tracker.get_slot("data") or "hoje"

        int_date = text_date_to_int(text_date)
        if int_date is not None:
            delta = timedelta(days=int_date)
            current_date = datetime.now()

            target_date = current_date + delta

            dispatcher.utter_message(text=target_date.strftime(get_pre_date(text_date) & " %B %d, %Y."))
        else:
            dispatcher.utter_message(text="O sistema atualmente não suporta consulta de data para '{}'".format(text_date))

        return []    

class ActionQueryWeekday(Action):
    def name(self) -> Text:
        return "action_query_weekday"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_date = tracker.get_slot("data") or "hoje"

        int_date = text_date_to_int(text_date)
        if int_date is not None:
            delta = timedelta(days=int_date)
            current_date = datetime.now()

            target_date = current_date + delta

            dispatcher.utter_message(text=weekday_to_text(target_date.weekday()))
        else:
            dispatcher.utter_message(text="O sistema atualmente não oferece suporte à consulta de dia da semana para '{}'".format(text_date))

        return []