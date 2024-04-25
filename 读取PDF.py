import PyPDF2


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ""

        for page in range(0, num_pages):
            page_obj = reader.pages[page]
            text += page_obj.extract_text()

    return text


# 使用函数读取PDF文件
file_path = r'杨豪-成都-软件测试.pdf'  # 替换为你的PDF文件路径
pdf_text = read_pdf(file_path)
print(pdf_text)
