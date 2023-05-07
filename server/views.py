from base64 import b64decode

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
from io import BytesIO
from time import time
from hashlib import md5

from server.models import Image
from server.serializers import ImageSerializer
from server.functions.ocr import pytesseract_read_image


@api_view(["POST"])
def read_image(request):

    try:
        raw_img = b64decode(request.data["image"].replace(";", "/"))
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    image = Image.open(BytesIO(raw_img))
    text = pytesseract_read_image(image)
    key = md5(str(time()).encode()).hexdigest() + str(round(time()))
    serializer = ImageSerializer(data=dict(id=key, text=text))

    if serializer.is_valid():
        serializer.save()
        print(f"read success: {key}")
        return Response(dict(id=key, text=text))

    print(f"read fail: {key}")
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def summarize_image(request, key):

    try:
        product = Image.objects.get(pk=key)
    except Image.DoesNotExist:
        print(f"summ fail: {key}")
        return Response(status=status.HTTP_404_NOT_FOUND)

    print(f"summ success: {key}")
    return Response({
        "text": "summarized"
    })
