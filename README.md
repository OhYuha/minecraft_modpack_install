# minecraft_modpack_install
## 마인크래프트 모드팩 설치 프로그램
마인크래프트의 모드팩을 설치하기 위한 프로그램입니다.

모드팩 개발자분은 아래의 사항을 따라 주시고 이용자분께서는 개발자분이 주시는 파일을 실행하시면 됩니다.

* python 설치
* PyInstaller 설치
* 모드팩에 넣을 모든 모드

다 설치하셨으면
1. 소스 코드 폴더에서 data폴더에 모드를 넣는다.
2. 소스 코드 폴더에서 cmd나 powershall을 실행하고
3. `pyinstaller --onefile --icon="icon.ico" --add-data "data;data" main.py` 을 입력한다.
4. dist폴더의 main.exe파일을 확인한다.

본 프로그램은 BSD-3 라이센스로 배포합니다.
