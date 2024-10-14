import os
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from examples import examples

embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    embeddings,
    Chroma,
    k=5,
    input_keys=["question"],
)

example_prompt = PromptTemplate(
    input_variables=["question", "query"],
    template="Question: {question}\nCypher query: {query}"
)

def create_few_shot_prompt():
    '''Create a prompt template. The suffix provides dynamically selected prompt examples using similarity search'''
    
    prefix = """
    Task: Generate Cypher statement to query a graph database.

    Instructions:
    Use only the provided relationship types and properties in the schema. Do not use any other relationship types or properties that are not provided.
    {schema}
    Before constructing any query, always refer to the examples. Ensure that the structure, use of indices, and result formatting strictly follow the examples provided. The examples must guide every part of the query, including how to handle indexes and how to format the results.
    Generally, the use of properties and relationships is intended for matching nodes. When responding to a query, you should not return the specific properties directly (like birthDate or other specific attributes). Instead, return the `text` property from the node where the relevant property (e.g., birthDate) is located. Your task is to find the node that contains the property and return the associated `text` field.
    For multimedia-related queries (images, videos, audios, and documents), always follow the examples and structure the query accordingly. If multimedia elements are involved, gather the corresponding multimedia nodes linked to the main entity using relationships like `HAS_MULTIMEDIA` and return them categorized under the fields `imagenes`, `videos`, `audios`, and `documentos`, depending on the type of multimedia. Make sure to collect the appropriate links and descriptions for each type, as seen in the provided examples.
    For example, if the question is asking for an author's birthdate, your query should identify the node with the `birthDate` property and then return the `text` field of that node. Similarly, if the question asks for multimedia content associated with an author, return the multimedia categorized as images, videos, audios, and documents, ensuring proper formatting.
    You will see several examples demonstrating how this works, and it is crucial that you follow them closely.
    Always avoid generating a query without first consulting the examples.
    Never generate a query with the prefix: 'Cypher query: ' — go straight to the query, to avoid syntax errors.

    Note:
    Do not include any explanations or apologies in your responses.
    Do not respond to any questions that ask anything other than for you to construct a Cypher statement.
    Do not include any text except the generated Cypher statement.

    Examples: Here are a few examples of generated Cypher statements for particular questions:
    """

    FEW_SHOT_PROMPT = FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt = example_prompt,
        prefix=prefix,
        suffix="Question: {question}, \nCypher Query: ",
        input_variables =["question","schema", "query"],
    )
    return FEW_SHOT_PROMPT

# Test the FewShotPromptTemplate

# prefix = """
# Task: Generate Cypher statement to query a graph database.

# Instructions:
# Use only the provided relationship types and properties in the schema. Do not use any other relationship types or properties that are not provided.
# {schema}
# Before constructing any query, always refer to the examples. Ensure that the structure, use of indices, and result formatting strictly follow the examples provided. The examples must guide every part of the query, including how to handle indexes and how to format the results.
# Generally, the use of properties and relationships is intended for matching nodes. When responding to a query, you should not return the specific properties directly (like birthDate or other specific attributes). Instead, return the `text` property from the node where the relevant property (e.g., birthDate) is located. Your task is to find the node that contains the property and return the associated `text` field.
# For multimedia-related queries (images, videos, audios, and documents), always follow the examples and structure the query accordingly. If multimedia elements are involved, gather the corresponding multimedia nodes linked to the main entity using relationships like `HAS_MULTIMEDIA` and return them categorized under the fields `imagenes`, `videos`, `audios`, and `documentos`, depending on the type of multimedia. Make sure to collect the appropriate links and descriptions for each type, as seen in the provided examples.
# For example, if the question is asking for an author's birthdate, your query should identify the node with the `birthDate` property and then return the `text` field of that node. Similarly, if the question asks for multimedia content associated with an author, return the multimedia categorized as images, videos, audios, and documents, ensuring proper formatting.
# You will see several examples demonstrating how this works, and it is crucial that you follow them closely.
# Always avoid generating a query without first consulting the examples.
# Never generate a query with the prefix: 'Cypher query: ' — go straight to the query, to avoid syntax errors.

# Note:
# Do not include any explanations or apologies in your responses.
# Do not respond to any questions that ask anything other than for you to construct a Cypher statement.
# Do not include any text except the generated Cypher statement.

# Examples: Here are a few examples of generated Cypher statements for particular questions:
# """

# FEW_SHOT_PROMPT = FewShotPromptTemplate(
#     example_selector = example_selector,
#     example_prompt = example_prompt,
#     prefix=prefix,
#     suffix="Question: {question}, \nCypher Query: ",
#     input_variables =["question","schema", "query"],
# )