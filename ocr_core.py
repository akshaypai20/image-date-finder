try:
    from PIL import Image
except ImportError:
    import Image

import re
import pytesseract
from datetime import datetime

import numpy as np
import pytesseract
#import cv2

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """

    pil_image = Image.open(filename)

    img = pil_image

    text = pytesseract.image_to_string(img, lang="eng")  
   
    #print(text)

# We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
'''
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Rescale the image
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Apply blur to smooth out the edges
    img = cv2.medianBlur(img, 3)

    # Apply threshold to get image with only b&w (binarization)
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    '''

def dateformats():
    "Yield all combinations of valid date formats."

    years = ("%Y", "%y")
    months = ("%b", "%B", "%m")
    day = "%d"
    seps = (" ", "/", "-", ".")

    for year in years:
        for month in months:
            for args in ((day, month), (month, day)):
                for sep in seps:
                    date = sep.join(args)
                    yield sep.join([date,year]).strip()
		
def getMatches(s):

    matched_list = []
    matches = re.findall(r"([\d]{1,2}|[a-zA-Z]{3})(/|-|\\|\s|\.)([\d]{1,2}|[a-zA-Z]{3})(/|-|\\|\s|\.)([\d]{2,4})", s)
    
    for match  in matches:
        combined_match = ""
        for word in match:
            combined_match += word
        matched_list.append(combined_match)
    return matched_list

def str2date(filename):

    s = ocr_core(filename)
    "Parse a string into a datetime object."
    match = re.search(r"([\d]{1,2}|[a-zA-Z]{3})(/|-|\\| |\.)([\d]{1,2}|[a-zA-Z]{3})(/|-|\\| |\.)([\d]{2,4})", s)
    #print(matches)
    if match is None:
       return "date not detected"

    #dateformats = get_dateformats(
    for fmt in dateformats():
        try:
            matched = datetime.strptime(match.group(), fmt)
            return str(matched.date())+" recognized date"
        except ValueError:
            pass

    return match.group()+" unrecognized date"

def checkConf(filename):
    return str2date(filename)
	
#print(str2date('images/adc1b1d1.jpeg'))
