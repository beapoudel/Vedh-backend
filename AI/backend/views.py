from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from backend.serializer import ImagesSerializer
from backend.models import images
import os
import json
api="AIzaSyC83ZzWxTViHv1VjYoxh2Td7B-RZUm_bDk"
print(api)
class AIapi(APIView):
 def post(self,request):
    topic=request.data.get('top')
    number=request.data.get('num')
    tone=request.data.get('ton')
    print(topic,number,tone)
    Response_json={
        "1":{
            "mcq":"Multiple choice Question",
            "option":{
                "a":"Choice here",
                "b":"Choice here",
                "c":"Choice here",
                "d":"Choice here",
            },
            "correct":"correct answer",
        },
        "2":{
            "mcq":"Multiple choice Question",
            "option":{
                "a":"Choice here",
                "b":"Choice here",
                "c":"Choice here",
                "d":"Choice here",
            },
            "correct":"correct answer",
        },
        "3":{
            "mcq":"Multiple choice Question",
            "option":{
                "a":"Choice here",
                "b":"Choice here",
                "c":"Choice here",
                "d":"Choice here",
            },
            "correct":"correct answer",
        }
    }
    Template= """
    You are expert in making quiz, So please make a quiz on topic {topic},number of questioin should be{number} in {tone} tone.Make sure the question are not repeated and check all the question to be conforming the text as well.Make sure the formate your response like Response_json below and use it as a guid. Ensure to make {number} MCQs  
    ###Response_json
    {response_json}
    """

    client=ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api
    )
    prompt=PromptTemplate(
        input_variables=["topic","number","tone","response_json"],
        template=Template
    )

    chain=LLMChain(llm=client,prompt=prompt)
    result=chain.invoke({"topic": topic, "number":number, "tone":tone,"response_json": json.dumps(Response_json)})
    print(result['text'])
    raw_text = result['text']
    cleaned_text = raw_text.strip("```json").strip("```")
    print(cleaned_text)

    return Response(json.loads(cleaned_text))
 
class Userapi(APIView):
   def post(self,request):
     name =request.data.get('name')
     email=request.data.get('email')
     if images.objects.count()==10:
       return Response(2)
     if images.objects.filter(email=email).exists():
        print("alredy there")
        return Response(1)
     data={'name': name,'email': email}
     serializer= ImagesSerializer(data=data)
     if serializer.is_valid():
       serializer.save()
       return Response("Data saved")
     return Response(serializer.errors)
