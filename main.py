from langchain_community.llms import Replicate
from langchain.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from db import create_db
import os



REPLICATE_API_TOKEN = "r8_DZzA1EuUx7dVspukZonTgADPygqUMs42AViMB"
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
llama2_13b_chat = "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d"

llm = Replicate(    
    model=llama2_13b_chat,
    model_kwargs={"temperature": 0.01, "top_p": 1, "max_new_tokens":500}
)


create_db()

db = SQLDatabase.from_uri("sqlite:///bank_data.db", sample_rows_in_table_info=0)

PROMPT_SUFFIX = """
Only use the following tables:
{table_info}

Question: {input}"""

# Set up SQLDatabaseChain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, return_sql=True, 
                                     prompt=PromptTemplate(input_variables=["input", "table_info"], 
                                                           template=PROMPT_SUFFIX))
import langchain
langchain.debug = True

# first question
db_chain.run("How many users have a 69 balance?")
