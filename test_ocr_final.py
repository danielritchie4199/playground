import os
from PIL import Image
import pytesseract

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def test_ocr():
    image_path = "ADsP_Y/ADsP_Y/ADsP_윤종식_페이지_016.png"
    
    if os.path.exists(image_path):
        print(f"이미지 파일 존재: {image_path}")
        try:
            image = Image.open(image_path)
            print(f"이미지 크기: {image.size}")
            
            # OCR 테스트 - 영어만 먼저 시도
            print("영어 OCR 시도 중...")
            text_eng = pytesseract.image_to_string(image, lang='eng')
            print(f"영어 텍스트 길이: {len(text_eng)}")
            print("영어 텍스트 샘플:")
            print(text_eng[:200])
            
            # 한국어 OCR 시도
            print("\n한국어 OCR 시도 중...")
            text_kor = pytesseract.image_to_string(image, lang='kor')
            print(f"한국어 텍스트 길이: {len(text_kor)}")
            print("한국어 텍스트 샘플:")
            print(text_kor[:200])
            
            # 한국어+영어 OCR 시도
            print("\n한국어+영어 OCR 시도 중...")
            text_kor_eng = pytesseract.image_to_string(image, lang='kor+eng')
            print(f"한국어+영어 텍스트 길이: {len(text_kor_eng)}")
            print("한국어+영어 텍스트 샘플:")
            print(text_kor_eng[:200])
            
            # 결과를 파일로 저장
            with open("ocr_test_result.txt", "w", encoding="utf-8") as f:
                f.write("=== 영어 OCR 결과 ===\n")
                f.write(text_eng)
                f.write("\n\n=== 한국어 OCR 결과 ===\n")
                f.write(text_kor)
                f.write("\n\n=== 한국어+영어 OCR 결과 ===\n")
                f.write(text_kor_eng)
            
            print("\n테스트 결과가 ocr_test_result.txt에 저장되었습니다.")
            
        except Exception as e:
            print(f"오류 발생: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"파일이 존재하지 않음: {image_path}")

if __name__ == "__main__":
    test_ocr() 