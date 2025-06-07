from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def ai(transcription, language, addicional_infos=""):
    template = PromptTemplate.from_template(
        '''
        I have a video transcription, and I need you to summarize it in {language}.

        Here is the transcription: {transcription}

        Please ensure the summary focuses on these key points: {addicional_infos}.

        Keep the summary concise, accurate, and aligned with the requested language. 
        If any information is unclear or insufficient in the transcription, state that explicitly rather than guessing.
        '''
    )

    prompt = template.format(language=language, transcription=transcription, addicional_infos=addicional_infos)

    llm  =  ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5)

    resposta = llm.invoke(prompt)
    return resposta.content
