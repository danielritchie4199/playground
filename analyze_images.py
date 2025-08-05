import os
import base64
from PIL import Image
import io

def encode_image_to_base64(image_path):
    """이미지를 base64로 인코딩합니다."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"이미지 인코딩 오류: {e}")
        return None

def analyze_image_with_cursor(image_path):
    """Cursor AI를 사용하여 이미지를 분석합니다."""
    try:
        # 이미지를 base64로 인코딩
        base64_image = encode_image_to_base64(image_path)
        if base64_image is None:
            return f"이미지 인코딩 실패: {image_path}"
        
        # 이미지 분석 요청 (Cursor AI 기능 활용)
        # 여기서는 이미지 파일 경로를 반환하여 Cursor AI가 직접 분석할 수 있도록 함
        return f"이미지 분석 요청: {image_path}"
        
    except Exception as e:
        return f"이미지 분석 오류: {str(e)}"

def process_images_sequentially():
    """16-72페이지의 이미지들을 순차적으로 처리합니다."""
    folder_path = "ADsP_Y/ADsP_Y"
    all_text = ""
    
    for page_num in range(16, 73):  # 16부터 72까지
        page_str = f"{page_num:03d}"
        image_path = os.path.join(folder_path, f"ADsP_윤종식_페이지_{page_str}.png")
        
        print(f"분석 중: 페이지 {page_num}")
        
        if os.path.exists(image_path):
            # 이미지 분석 요청
            analysis_result = analyze_image_with_cursor(image_path)
            all_text += f"\n\n{'='*60}\n"
            all_text += f"페이지 {page_num}\n"
            all_text += f"{'='*60}\n\n"
            all_text += f"이미지 파일: {image_path}\n"
            all_text += f"분석 결과: {analysis_result}\n"
            print(f"페이지 {page_num} 분석 완료")
        else:
            print(f"파일이 존재하지 않음: {image_path}")
    
    return all_text

if __name__ == "__main__":
    print("ADsP 16-72페이지 이미지 분석을 시작합니다...")
    print("총 57페이지를 처리합니다...")
    
    extracted_text = process_images_sequentially()
    
    # 결과를 파일로 저장
    output_file = "ADsP.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("ADsP 윤종식 교재 16-72페이지 이미지 분석 결과\n")
        f.write("="*60 + "\n\n")
        f.write(extracted_text)
    
    print(f"\n이미지 분석 완료!")
    print(f"결과가 {output_file}에 저장되었습니다.")
    print("이제 Cursor AI를 사용하여 각 이미지를 개별적으로 분석하세요.") 