import os
from PIL import Image
import pytesseract

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def test_single_image():
    image_path = "ADsP_Y/ADsP_Y/ADsP_윤종식_페이지_016.png"
    
    if os.path.exists(image_path):
        print(f"이미지 파일 존재: {image_path}")
        try:
            image = Image.open(image_path)
            print(f"이미지 크기: {image.size}")
            
            # OCR 테스트
            text = pytesseract.image_to_string(image, lang='kor+eng')
            print("추출된 텍스트:")
            print(text)
            
            # 파일로 저장
            with open("test_output.txt", "w", encoding="utf-8") as f:
                f.write(text)
            print("테스트 결과가 test_output.txt에 저장되었습니다.")
            
        except Exception as e:
            print(f"오류 발생: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"파일이 존재하지 않음: {image_path}")

if __name__ == "__main__":
    test_single_image() 