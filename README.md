# PYTHON 영화 예매 프로그램

Tkinter 기반의 간단한 영화 예매 앱입니다. 사용자와 관리자가 각각 로그인하여 상영작 확인, 좌석 예매, 취소, 상영 편성 관리 기능을 체험할 수 있습니다.

## 실행 방법

```bash
python main.py
```

- 사용자: 회원가입 후 로그인해서 영화와 좌석을 선택하고 예매하거나 취소합니다.
- 관리자: 아이디 `admin@example.com`, 비밀번호 `admin123`으로 로그인해 상영작을 추가하거나 삭제하고 예매 현황을 확인합니다.

## VS Code에서 실행하기

1. VS Code에서 "파일 → 폴더 열기"를 선택하고 이 프로젝트 폴더를 엽니다.
2. 좌측 탐색기에서 `main.py`를 선택해 편집기를 엽니다.
3. 오른쪽 위 녹색 실행 버튼(재생 모양)을 눌러 실행하거나, 터미널을 열어 `python main.py`를 입력합니다.
4. 실행 후 나타나는 창에서 바로 회원가입과 로그인, 예매 기능을 시험할 수 있습니다.

## 내 문서/vscode_python 폴더에서 실행하기

1. Windows 탐색기에서 "내 문서"에 `vscode_python` 폴더를 만듭니다.
2. 이 폴더 안에 `main.py` 파일을 붙여넣습니다.
3. VS Code에서 "파일 → 폴더 열기"로 `내 문서/vscode_python`을 선택합니다.
4. 편집기에서 `main.py`를 연 뒤 오른쪽 위 실행 버튼을 누르거나 터미널에 `python main.py`를 입력합니다.
5. 앱 창이 뜨면 바로 회원가입과 로그인, 예매를 해 볼 수 있습니다.

## VS Code에서 패치 적용이 안 될 때
1. GitHub나 에디터에서 "Apply changes"가 실패하면, 이 저장소의 `main.py` 전체 내용을 복사해서 로컬 `main.py`에 그대로 붙여넣으세요.
2. 붙여넣은 뒤 파일의 첫 줄이 `import tkinter as tk`로 시작하는지 확인하고 저장하세요.
3. VS Code 터미널을 열어 `python main.py`를 입력해 실행하면 됩니다.

## GitHub에 올리기
1. GitHub에 새 저장소를 만듭니다.
2. 터미널에서 이 프로젝트 폴더로 이동한 뒤 `git init`을 한 번만 입력합니다.
3. `git remote add origin https://github.com/계정/저장소.git`처럼 원격을 등록합니다.
4. `git add .`으로 파일을 올릴 목록에 넣고 `git commit -m "first commit"`으로 저장합니다.
5. `git push -u origin main`을 입력해 GitHub에 올립니다. 기본 브랜치 이름이 `master`면 `git push -u origin master`를 써 주세요.
