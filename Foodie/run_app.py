from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-517280283250-517151581972-516736065809-6f37c4a1df0ecb3aa9b1e10dd8a7e94b', #app verification token
							'xoxb-517280283250-516736066865-kODLJiSWGq0vX6tdfxIfxL6i', # bot verification token
							'cyhtM54NFDEBlxRlklsyKIU5', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
