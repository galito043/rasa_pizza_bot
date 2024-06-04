from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionToppingsWanted(Action):

    def name(self) -> Text:
        return "action_toppings_wanted"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        toppings = tracker.get_slot("toppings")

        if toppings:
            toppings_str = ', '.join(toppings)
            dispatcher.utter_message(text=f"The toppings are {toppings_str}.")
        else:
            dispatcher.utter_message(text="You haven't told me what toppings you want yet.")
        return []
