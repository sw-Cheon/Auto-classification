# Auto-classification

## python을 이용한 사진, 동영상 날짜별 자동 분류 프로그램
![Auto_classification](https://user-images.githubusercontent.com/63433646/110236478-665be180-7f79-11eb-9925-316ce621453a.png)

	Auto_classification폴더 안에 있는 APV폴더에 변환을 원하는 파일을 넣고 프로그램을
	실행시키면 각 파일의 속성 정보에서 생성날짜(혹은 최종수정날짜) 등을 읽어와 각 파일의
	이름을 날짜로 변환하여 바탕화면에 저장해주는 프로그램입니다.(날짜가 중복되는 경우 _1, _2로 저장)
	* 지원되는 파일형식 : jpg, jpeg, png, gif, avi, mp4, mpeg

* 사용방법
	* git clone으로 code를 내려받고 Auto_classification 폴더 안에 있는 Auto_classification.exe파일을 실행시킵니다.

> 필요한 모듈
>> pyqt5   
>> Pillow   
>> shutil   