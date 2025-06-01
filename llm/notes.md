# PlayList 
https://www.youtube.com/watch?v=xbaYCf2FHSY&list=PLPTV0NXA_ZSgsLAr8YCgCwhPIJNNtexWu&index=5&ab_channel=Vizuara



Based on the book:
  Building a Large language Model (From Scratch) - Sebastian Raschika

what is LLM?
Deep Neural Network (DNN) - trained on large amount of text data.
"large" - due to the size of paramaters. current billions to trillions
"language" NLP(used to be for specific task) - now handles range of tasks

Transformer Architecture    

[LLM] vs [GenAI] vs [Deep Learning(DL)] vs [Machine Learning]

---hierarchy---
AI -> ML -> DL -> LLM(Text only)

GenAI == LLM + DL

LLM applications
 - content genration
 - Sentiment Analysis
 - Chatbots/Virtual Assistants
 - Machine translation
 - (New)Novel text genration


 --- Chapter 3 ---------
 PreTraining + Fine tuning -> LLM

 --- Chapter 4 Transformer ---------
 Input text -> preprossing -> encoder -> embeddings -> decoder -> output layer

 encoder -> encodes input text into vectors
 decoder -> geneate output text from encoded vectors

 BERT -> Bidirectional encoder representations from Transformers
  > predicts hidden words in a given sentence
  > great for Sentiment Analysis

 GPT -> Generative pretrained Transformer
  > geneate near words

  Note: Not all LLM are Transformers, LLM can be based on recurrent/convolutional Architecture



--- Chapter 5 GPT ---------
Zero Shot -> ability to geenrate completelly unseen tasks without prior examples
Few Shot -> Learning from a minimum number of examples, which user provides as input.

GPT trained for "next-work" but has "emergent-behavior" e.g. language translation


--- Chapter  Stages of building LLM ---------
 STAGE 1 (Buidling on LLM)
 data prepartion & sampling > attention mechanism > llm architecture

 STAGE 2 (Foundational model)
 Traning loop > model evaluation > load pretained weights

 STAGE 3 (Finetuning)
 classifer | personal assistant


--- Chapter 7  Code an LLM Tokenizer -------
coding simple tokenizer

--- Chapter 8 byte pair enconding -------
