




from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


        
from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.chat_models import ChatOpenAI


llm = model = ChatOpenAI(temperature=0,model="gpt-4o")



def convert_to_json(receipt_detail):
  
  parser = JsonOutputParser()

  prompt = PromptTemplate(
      template="""
      
      Read the img receipt provided to you delimited by triple backticks ``` and return a JSON object with ( Date, Items,total,spending_insights) from the \n{format_instructions}\n{receipt_detail} receipt.

      If any of these keys are missing, assign "NONE" in double quotes  as their value.
      Always format Items as an array of objects, each containing item name and price.
      provide spending insights in spending_insights key.
      
      Example format:
      {{
        "total":0.0,
        "Date": null,
        "Items": [
          {{
            "item_name": "example_item",
            "price": 0.0
          }}
        ],
        "spending_insights":""
      }}
      
      receipt: ```{receipt_detail}```
      """,
      input_variables=["receipt_detail"],
      partial_variables={
          "format_instructions": parser.get_format_instructions().replace("{", "{{").replace("}", "}}")
      },
  )

  chain = prompt | model | parser

  result = chain.invoke({"receipt_detail": receipt_detail})
  return result







      # Return a JSON object with a (Location,Time,Date,item) of the following \n{format_instructions}\n{receipt_detail}\n receipt.