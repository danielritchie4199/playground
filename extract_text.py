import os
import sys
from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    """이미지에서 텍스트를 추출합니다."""
    try:
        # 이미지 열기
        image = Image.open(image_path)
        
        # OCR로 텍스트 추출 (한국어 + 영어)
        text = pytesseract.image_to_string(image, lang='kor+eng')
        
        return text
    except Exception as e:
        return f"오류 발생: {str(e)}"

def process_images_in_range(start_page, end_page, folder_path):
    """지정된 페이지 범위의 이미지들을 처리합니다."""
    all_text = ""
    
    for page_num in range(start_page, end_page + 1):
        # 페이지 번호를 3자리로 포맷팅 (예: 016, 017, ...)
        page_str = f"{page_num:03d}"
        image_path = os.path.join(folder_path, f"ADsP_윤종식_페이지_{page_str}.png")
        
        if os.path.exists(image_path):
            print(f"처리 중: {image_path}")
            text = extract_text_from_image(image_path)
            all_text += f"\n\n=== 페이지 {page_num} ===\n"
            all_text += text
        else:
            print(f"파일이 존재하지 않음: {image_path}")
    
    return all_text

if __name__ == "__main__":
    folder_path = "ADsP_Y/ADsP_Y"
    start_page = 16
    end_page = 72
    
    print(f"페이지 {start_page}부터 {end_page}까지 텍스트 추출을 시작합니다...")
    
    extracted_text = process_images_in_range(start_page, end_page, folder_path)
    
    # 결과를 파일로 저장
    output_file = "ADsP_.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(extracted_text)
    
    print(f"텍스트 추출 완료. 결과가 {output_file}에 저장되었습니다.") 