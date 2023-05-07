from base64 import b64decode

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image as PILImage
from io import BytesIO
from time import time
from hashlib import md5
from server.functions.advanced_funcs import get_summary, get_lang, get_keywords

from server.models import Image
from server.serializers import ImageSerializer
from server.functions.ocr import pytesseract_read_image


@api_view(["POST"])
def read_image(request):

    print("[READ] start read")

    try:
        raw_img = b64decode(request.data["image"].replace(";", "/"))
    except Exception as e:
        print("[READ] failed")
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    print("[READ] convert")
    image = PILImage.open(BytesIO(raw_img))
    text = pytesseract_read_image(image)
    key = md5(str(time()).encode()).hexdigest() + str(round(time()))
    serializer = ImageSerializer(data=dict(id=key, text=text))
    print(f"[READ] key: {key}")

    if serializer.is_valid():
        print("[READ] start save")
        serializer.save()
        print("[READ] save finish")
        return Response(dict(id=key, text=text))

    print("[READ] invalid format")
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def summarize_image(request, key):

    print(f"[SUMMARIZE] start on {key}")

    try:
        image = Image.objects.get(pk=key)
    except Image.DoesNotExist:
        print("[SUMMARIZE] key does not exist")
        return Response(status=status.HTTP_404_NOT_FOUND)

    print("[SUMMARIZE] get summary")
    summary = get_summary(dict(ImageSerializer(image).data)["text"])

    print("[SUMMARIZE] finish")
    return Response(dict(text=summary))


@api_view(["GET"])
def get_image_lang(request, key):

    print(f"[LANG] start on {key}")

    try:
        image = Image.objects.get(pk=key)
    except Image.DoesNotExist:
        print("[LANG] key does not exist")
        return Response(status=status.HTTP_404_NOT_FOUND)

    print("[LANG] get summary")
    lang = get_lang(dict(ImageSerializer(image).data)["text"])

    print("[LANG] finish")
    return Response(dict(text=f"The language is {lang}."))


@api_view(["GET"])
def get_image_keywords(request, key):

    print(f"[KEYWORDS] start on {key}")

    try:
        image = Image.objects.get(pk=key)
    except Image.DoesNotExist:
        print("[KEYWORDS] key does not exist")
        return Response(status=status.HTTP_404_NOT_FOUND)

    print("[KEYWORDS] get summary")
    keywords = get_keywords(dict(ImageSerializer(image).data)["text"])

    print("[KEYWORDS] finish")
    return Response(dict(text=f"The keywords are: {keywords}."))
