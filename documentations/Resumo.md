## Reference
https://github.com/RasaHQ/financial-demo
https://github.com/PacktPublishing/Conversational-AI-with-RASA

## Dictionary:
- GPT - Generative Pre-trained Transformer
- BERT - Bidirectional Encoder Representations from Transformers

- ELMo - Embeddings from Language Models
- LSTM - long short-term memory
- RNN - recurrent neural network
- DNN - 
- CNN - convolutional neural network
- GANs - Generative adversarial networks
- ANN - artificial neural network

- DM - Dialogue Management
- ER - entity recognition
- NLU - natural language understanding
- From sequences to categories (algorithms) - TextCNN, TextRNN
- Seq2Seq - Synchronous sequence to sequence
- CNNs - convolutional neural networks
- NLG - Natural Language Generation

### Models:
- Stochastic Gradient Descent (SGD)
- Nearest Neighbors (NN)
- Support Vector Classification (SVC)
- Random Forest (RF)
- Adaptive Boosting (AdaBoost)

## Introduction to the Rasa framework

Rasa is an open source ML framework to construct chatbots and intelligent assistants.

Rasa's modular and flexible design enables developers to easily build new extensions and
functionalities. Rasa covers almost all the functions needed for building a conversation
system and is currently the mainstream open source conversational system framework.

### The Rasa framework consists of mainly four parts, outlined as follows:
- NLU: Extract user's intent and key context information
- Core: Choose the best response and action according to dialogue history
- Channel and action: Connect chatbot to users and backend services
- Helper functions such as Tracker Store, Lock Store, and Event Broker

### Chatbot basics

A chatbot is a software system that is used to have a conversation with people via text or
speech. Chatbots are used for various purposes, including customer service, enterprise
operations, and healthcare. According to the different goals, chatbots have two main
types: task-oriented bots and chitchat bots. Task-oriented bots have the goal of finishing
specific tasks by interacting with people, such as booking a flight ticket for someone, while
chitchat bots are more like human beings—their goal is to respond to users' messages
smoothly, just as with chitchat between people.

task-oriented bots: Task-oriented bots have the goal of finishing
specific tasks by interacting with people, such as booking a flight ticket for someone

chitchat bots: chitchat bots are more like human beings

Alicebot - Artificial Linguistic Internet Computer Entity => Important!

Rasa NLU converts a user's input into intents and entities


### Dialogue management in Rasa:

- Dialogue state tracking: updates the dialogue state according to the previous round of dialogue and the previous
round of system actions, as well as the user's intentions and entities in the current round
- Dialogue policy: is responsible for outputting dialogue actions according to the
dialogue state
- Dialogue action: Is based on the decision of the dialogue strategy to
interact with the backend interface to complete the actual task execution
- Dialogue result output: Outputs the result of the system operation in a user-friendly way

### Components of Rasa's dialogue management system
domain, story, action, slot, and policy

### Cover the follow topics:
- Understanding the universe of your bot (domain)
- Training data for dialogue management (stories)
- Reacting to user input (action)
- Understanding the memory of your bot (slots)
- Understanding the decision-maker of your bot (policies)
- Building custom actions using Rasa SDK
- Using channels to communicate with instant messaging software
- Building a tell-the-time bot

