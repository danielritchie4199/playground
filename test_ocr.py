import os
from PIL import Image
import pytesseract

# Tesseract 경로 설정 (Windows의 경우)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def test_ocr():
    image_path = "ADsP_Y/ADsP_Y/ADsP_윤종식_페이지_016.png"
    
    if os.path.exists(image_path):
        print(f"이미지 파일 존재: {image_path}")
        try:
            image = Image.open(image_path)
            print(f"이미지 크기: {image.size}")
            
            # OCR 테스트
            text = pytesseract.image_to_string(image, lang='kor+eng')
            print("추출된 텍스트:")
            print(text[:500])  # 처음 500자만 출력
            
        except Exception as e:
            print(f"오류 발생: {e}")
    else:
        print(f"파일이 존재하지 않음: {image_path}")

if __name__ == "__main__":
    test_ocr() 