# Simple RAG Application

Welcome to the repository for a simple RAG (Retrieval-Augmented Generation) application designed to provide music enthusiasts with personalized song recommendations. This application utilizes a combination of lyrical snippets and music genre information to find and suggest songs that closely match user queries.

## Features

- Retrieve song suggestions based on a corpus of song metadata.
- Utilize Jaccard similarity to evaluate content relationships.
- Engage users with interactive input prompts for personalized queries using llama3 LLM

### Prerequisites

  - Make sure you have Python and `pip` installed. Visit Python's [official documentation](https://www.python.org/downloads/) for installation instructions. Then, install the required packages:

  ```bash
  pip install langchain_community
  ```
  - ollama with llama3

## Installation

  * Clone the repository:
  * Navigate to the repository folder:
    ```bash
    cd simple-rag-application
    ```
  * Run the application:
    ```bash
    python main.py
    ```

### Corpus
The application comes with a built-in corpus containing a curated list of songs. Each song entry includes the title, a brief lyric excerpt, and the genre. This corpus is crucial for the functioning of the RAG model and can be easily expanded or modified to refine recommendations.

## Author
  <https://github.com/saxenaakansha30> - Akansha Saxena

## Acknowledgments
  * Thanks to everyone who has contributed to the development of the Ollama platform.
  * Credit to the langchain team.

## Sample Examples:=

- I am thinking of something dark blue and smoky eyes
- I am thinking of something Pop, desert and light
- I don’t want to listen any song

