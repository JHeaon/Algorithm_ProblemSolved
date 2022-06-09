import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장") # 창 이름설정
root.geometry("640x480") # 가로 * 세로
menu = Menu(root)

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장



menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file) # command에는 함수명만 적어야함!
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit())
menu.add_cascade(label="파일(F)", menu=menu_file) # cascade를 통해 메뉴창이름이 File인 것을 만들고 그 기능을 menu에 넣음

# 편집 서식 보기 도움말
menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식(O)")
menu.add_cascade(label="보기(V)")
menu.add_cascade(label="도움말")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()


