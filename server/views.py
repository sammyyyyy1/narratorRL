from base64 import b64decode

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
from io import BytesIO

from .models import ImageText
from .serializers import ProductSerializer
from .functions.ocr import pytesseract_read_image


@api_view(["POST"])
def read_image(request):

    try:
        raw_img = b64decode(request.data["image"].replace(";", "/"))
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    image = Image.open(BytesIO(raw_img))
    # print(image.size)
    # if image.size[0] > image.size[1]:
    #     print("rotate")
    #     image = image.rotate(270)
    #     print(image.size)

    data = pytesseract_read_image(image)
    with open("res.jpg", "wb") as img_file:
        img_file.write(raw_img)

    return Response({"text": data})

    # url = b64decode(b64).decode("utf-8")
    # url_parts = url.split("/")
    # name = url_parts[0] + url_parts[2]
    # print(url)
    #
    # try:
    #     product = ImageText.objects.get(pk=name)
    # except ImageText.DoesNotExist:
    #     print("[SEARCH] - Start")
    #     scrape_res = translate(url_parts[0] + url_parts[2], scrape(url_parts[0], url_parts[2]))
    #     print("[SEARCH] - Completed")
    #     serializer = ProductSerializer(data=scrape_res)
    #     if serializer.is_valid():
    #         print("[DATA] - Valid")
    #         serializer.save()
    #         product = ImageText.objects.get(pk=name)
    #     else:
    #         print("[DATA] - Invalid")
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    # data = dict(ProductSerializer(product).data)
    return Response({
        "id": "hi"
    })


@api_view(["GET"])
def summarize_image(request, image_id):

    try:
        product = ImageText.objects.get(pk=image_id)
    except ImageText.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response({
        "tdb": "freddy"
    })
