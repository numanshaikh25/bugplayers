from email import message
from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.http import JsonResponse, HttpResponse
# Create your views here.
import os
import google.cloud.dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
import json 

# credential_path="./INeuron Hackathon/bugplayers/chatbot/private_key.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

DIALOGFLOW_PROJECT_ID='bugplayers-catm'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = '1'
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)



@api_view(["POST"])
def chatting(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    message = body.get("message")
    text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    return JsonResponse({"Reply":response.query_result.fulfillment_text})
