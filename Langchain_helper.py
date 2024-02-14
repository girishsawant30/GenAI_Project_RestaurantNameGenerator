
import vertexai
from vertexai.language_models import TextGenerationModel
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain_community.llms import VertexAI
import os


os.environ["GOOGLE_CLOUD_PROJECT"] = "fair-gist-408904"
os.environ["REGION_NAME"] = "us-central1"  # If applicable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\sawoo\\OneDrive\\Desktop\\Python\\fair-gist-408904-a23ea1a2e727.json"

llm = VertexAI(
    model_name="text-bison",
    max_output_tokens=1024,
    temperature=0.5
)

def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest one fancy name for this'
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated list"
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))