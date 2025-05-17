import pytesseract
from PIL import Image

tamil_to_eng_map = {
    'த': 'T', 'ந': 'N', 'ா': '',  # தநா = TN
    'அ': 'A', 'ஆ': 'AA', 'இ': 'I', 'ஈ': 'II',
    'உ': 'U', 'ஊ': 'UU', 'எ': 'E', 'ஏ': 'EE',
    'ஐ': 'AI', 'ஒ': 'O', 'ஓ': 'OO', 'ஔ': 'AU',
    'ஜ': 'J', 'ஷ': 'SH', 'ஸ': 'S', 'ஹ': 'H',
    'க': 'K', 'ங': 'NG', 'ச': 'C', 'ஞ': 'NJ',
    'ட': 'D', 'ண': 'N', 'த': 'T', 'ந': 'N',
    'ப': 'B', 'ம': 'M', 'ய': 'Y', 'ர': 'R',
    'ல': 'L', 'வ': 'V', 'ழ': 'ZH', 'ள': 'L',
    'ற': 'R', 'ன': 'N', 'ம்': 'M', 'க்': 'K',
    'ட்': 'T', 'ச்': 'C', 'ப்': 'B', 'ண்': 'N',
    '௧': '1', '௨': '2', '௩': '3', '௪': '4', '௫': '5',
    '௬': '6', '௭': '7', '௮': 'A', '௯': '9', '௦': '0'
}

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='tam')  # Tamil OCR
    return text.strip()

def transliterate_tamil_text(tamil_text):
    result = ""
    for char in tamil_text:
        if char in tamil_to_eng_map:
            result += tamil_to_eng_map[char]
        else:
            result += char
    return result

def translate_to_english(tamil_text):
    # Instead of using GoogleTranslator, use custom transliteration
    if not tamil_text:
        return ""
    return transliterate_tamil_text(tamil_text)
