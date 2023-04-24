# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
)

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
    
class ActionListaPedidos(Action):

    def name(self) -> Text:
        return "action_lista_pedidos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # print("****************************")
        # print(tracker)
        # print("############################")
        # print(domain)
        # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        text_date = tracker.get_slot("data") or "hoje"
        text_cenario_code = tracker.get_slot("cenario") or None

        int_date = text_date_to_int(text_date)
        dia = None
        if int_date is not None:
            delta = timedelta(days=int_date)
            current_date = datetime.now()

            target_date = current_date + delta

            dia = target_date.strftime("%d/%m/%Y")
            
            response = { "comando": "lista_pedidos", "data": dia, "cenario": text_cenario_code }

            data_formatada = {
                "data_formatada": dia
            }

            dispatcher.utter_message(response="utter_lista_pedidos", **data_formatada)
            dispatcher.utter_message("COMMAND=>" + str(response))
        else:
            dispatcher.utter_message(text="O sistema atualmente não suporta consulta de data para '{}'".format(text_date))

        return [SlotSet("data_formatada", dia)]
    
class ActionRemoveCenario(Action):

    def name(self) -> Text:
        return "action_remove_cenario"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return [SlotSet("cenario", None)]

