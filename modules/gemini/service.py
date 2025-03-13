from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from modules.gemini.model import ResponseModel
import os
from dotenv import load_dotenv
load_dotenv()

class GeminiService:
    def __init__(self):
        self.output_parser = PydanticOutputParser(pydantic_object = ResponseModel)
        self.format_instructions = self.output_parser.get_format_instructions()
        self.llm = ChatGoogleGenerativeAI(
            model=os.getenv("MODEL_ID"),
            temperature=os.getenv("TEMPERATURE"),
            google_api_key=os.getenv("API_KEY"),
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Extract information from the ID card image but if image is not an ID card, return None.\n{format_instructions}\n"),
            ("human", [
                {
                    "type": "text",
                    "text": "Extract information from the ID card image.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "data:image/png;base64,{image_data}"},
                },
            ]),
        ])

        self.chain = self.prompt | self.llm | self.output_parser

    def extract_text(self, base64_str: str):
        print(len(base64_str))
        data = self.chain.invoke({
            'image_data': base64_str,
            'format_instructions': self.format_instructions
        })
        if data.id_card is None:
            return None
        return data.id_card