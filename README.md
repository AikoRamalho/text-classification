# Project text-classification
This project explores the Hugging Face Datasets and Transformers libraries to work with text classification tasks. The main focus is on using the DistilBERT model for sentiment analysis on a dataset containing emotions.

## Introduction
In this project, we will:

1. Explore the datasets available in the Hugging Face Hub.
2. Load the emotion dataset and examine its structure.
3. Perform data preprocessing and understand how tokenization works.
4. Analyze the dataset and its class distribution.
5. Train a text classifier using the DistilBERT model for emotion classification.
## Dataset Exploration
First, we will list all the datasets available in the Hugging Face Hub and display the first 10.

## Loading the Emotion Dataset
Next, we load the emotion dataset and take a look at its structure.

## Data Inspection
We inspect the training dataset and explore its columns, features, and data types. We observe that the "text" column is of string data type, while the "label" column is a ClassLabel object that contains information about the class names and their mappings to integer values.

## Dataset Distribution
We examine the distribution of examples among the different emotion classes in the dataset. We notice that the dataset is heavily imbalanced, with "joy" and "sadness" appearing frequently, while "love" and "surprise" are much rarer.

## Text Length Analysis
We analyze the length of tweets in the dataset to understand the distribution of text length. We find that each tweet contains around 15 words, well below the maximum context size of 512 tokens for DistilBERT. We discuss the importance of truncation and its potential impact on model performance.

## Tokenization
We explain the concept of tokenization and introduce subword tokenization. We demonstrate how the tokenizer converts raw text into token IDs and how to convert tokens back into strings.

## Tokenizing the Whole Dataset
We tokenize the entire emotion dataset to prepare it for training. We use padding and truncation to ensure all sequences have the same length and create attention masks to help the model ignore padded parts of the input.

## Training a Text Classifier
Finally, we use the DistilBERT model as a feature extractor to obtain hidden states for each input sequence. We explain how to extract the "CLS" token's hidden state and use it as input features for training a text classifier.

## Conclusion
This project serves as a practical guide to working with text classification tasks using the Hugging Face Datasets and Transformers libraries. We demonstrate how to load, preprocess, tokenize, and analyze text data for emotion classification. By the end of the project, you will have a better understanding of how to utilize powerful NLP tools to build and train text classifiers for various applications.


