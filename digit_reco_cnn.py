import requests
import json
# from google.cloud import vision
import io
# import retinasdk
import os
import win32com.client as wincl

def detect_document(image):
    #export GOOGLE_APPLICATION_CREDENTIALS="/home/vishnu/Downloads/MyFirstProject-70a9ec5c77c9.json"
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()

    #with io.open(path, 'rb') as image_file:
     #   content = image_file.read()

    #image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))
    '''
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))
                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))
   '''
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return response


def txt_comp(answer_txt,key_txt):
        liteClient = retinasdk.LiteClient("4e5305c0-50e8-11ea-8f72-af685da1b20e")
        return liteClient.compare(answer_txt, key_txt)
def text_retuen(image):
    return "hello world"
def speak_the_text(text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)