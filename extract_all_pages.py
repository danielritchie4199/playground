import os
from PIL import Image
import pytesseract

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """이미지에서 텍스트를 추출합니다."""
    try:
        image = Image.open(image_path)
        # 한국어+영어 OCR 사용
        text = pytesseract.image_to_string(image, lang='kor+eng')
        return text
    except Exception as e:
        return f"오류 발생: {str(e)}"

def process_all_pages():
    """16-72페이지의 모든 이미지를 처리합니다."""
    folder_path = "ADsP_Y/ADsP_Y"
    all_text = ""
    
    for page_num in range(16, 73):  # 16부터 72까지
        page_str = f"{page_num:03d}"
        image_path = os.path.join(folder_path, f"ADsP_윤종식_페이지_{page_str}.png")
        
        print(f"처리 중: 페이지 {page_num}")
        
        if os.path.exists(image_path):
            text = extract_text_from_image(image_path)
            all_text += f"\n\n{'='*60}\n"
            all_text += f"페이지 {page_num}\n"
            all_text += f"{'='*60}\n\n"
            all_text += text
            print(f"페이지 {page_num} 완료 - 텍스트 길이: {len(text)}")
        else:
            print(f"파일이 존재하지 않음: {image_path}")
    
    return all_text

if __name__ == "__main__":
    print("ADsP 16-72페이지 텍스트 추출을 시작합니다...")
    print("총 57페이지를 처리합니다...")
    
    extracted_text = process_all_pages()
    
    # 결과를 파일로 저장
    output_file = "ADsP_.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("ADsP 윤종식 교재 16-72페이지 핵심 내용 요약\n")
        f.write("="*60 + "\n\n")
        f.write(extracted_text)
    
    print(f"\n텍스트 추출 완료!")
    print(f"결과가 {output_file}에 저장되었습니다.")
    print(f"총 {len(extracted_text)} 자의 텍스트가 추출되었습니다.") 