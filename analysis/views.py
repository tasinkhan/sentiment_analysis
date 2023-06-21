import json
from django.views.decorators.csrf import csrf_exempt
from setfit import SetFitModel
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @csrf_exempt
@api_view(['POST'])
def sentiment_analysis(request):
    # declaring sentiment value as None
    sentiment = None
    SENTIMENT_MAP = {
        0:"negative",
        1:"positive"
    }
    
    data = json.loads(request.body)
    text = data['text']
    print(text)
    # Checking either the text data is empty or contains only numeric values
    if not text:
        return Response({'detail':"Empty text can not be analyzed"}, status=status.HTTP_400_BAD_REQUEST)
    elif text.isnumeric():
        return Response({'detail':"Only numeric data can not be analyzed"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # set the specific model to analyze data(text-classification)
        model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
        prediction = model([text])
        # this model returns tensor object. so to retrieve the value we used .item() function.
        predicted_value = prediction.item()
        # grab the string representation from sentiment map using value from tensor object
        sentiment = SENTIMENT_MAP[predicted_value]
    
        return Response({"sentiment":sentiment})
