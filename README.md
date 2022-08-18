# 주제: 개 물림 사고 예방을 위한 강아지 분류 프로그램 <br>

## 1. 팀원
  팀장 : 이현민 <br>
  팀원 : 김성진 <br> <br>
  

## 2. Data 구조
![image](https://user-images.githubusercontent.com/67961082/183932830-746f0c9c-9c65-4f06-b9cd-1a419e3fb063.png)
<br>
<br>
<br>

## 3. Program Flow chart
![image](https://user-images.githubusercontent.com/67961082/183933332-acd9efc1-8bb4-4a17-a206-3cc427e24526.png)
<br>
<br>
<br>

## 4. 모델 성능

- Test loss: 0.076770223 <br>
- Test Acc : 97.80219893 <br>
- Val loss : 0.2315 <br>
- Val Acc  : 95.250 <br> <br>

![image](https://user-images.githubusercontent.com/67961082/183933423-e20361b5-e249-4f4a-affa-1c8c588eaf22.png)
<br>
<br>
<br>

## 5. 시연

### 5-1. 동영상<br>
1. leash -> leash_muzzle (영상 출처: https://www.youtube.com/watch?v=b-6V8QS7YpU&t=249s) <br> 

https://user-images.githubusercontent.com/67961082/185427251-f0de19e8-4d91-4a32-b4e1-f23d3810079c.mp4


<br>

2. more than two dogs (영상 출처: https://www.youtube.com/watch?v=xH9sN0Oc8GY&t=183s) <br> 



https://user-images.githubusercontent.com/67961082/185428227-eafc9c39-fa29-4e03-9b39-5ed0c1f508e2.mp4



<br>

## 5-2 실시간(웹캠) <br>

1. nothing <br>


https://user-images.githubusercontent.com/67961082/185427541-910da278-3b93-4ef1-987c-1e62031a0fe7.mp4



2. leash <br>



https://user-images.githubusercontent.com/67961082/185427574-60327e51-ffee-479f-a446-986c65f7ab86.mp4


<br>

## 6. 개선할 점

* 양질의 데이터셋 구축
  * 다양한 형태의 강아지 사진
  * 해상도가 높은 이미지
  * 보다 많은 데이터셋 구하기<br><br>
  
* 이미지 분류 속도 높이기
  * 실시간에서 보다 빠르게 분류할 수 있도록 Flow 최적화 작업 필요<br><br>  
  
* 모델의 서비스화
  * 모델을 CCTV에 연결
  * "nothing"으로 나온 결과 값을 저장하고 관리할 수 있는 페이지 만들기<br>
  
## 7. 느낀점

* 팀원의 중요성
  * 팀원간 활발한 대화
  * 같은 목표를 갖고 나아가는 팀 <br><br>
 
* 코드 분석 능력의 중요성
  * 구글링한 내용 적용
  * Yolov4 커스텀 하여 사용하기 <br><br>
  
* 데이터 전처리의 중요성
  * 영상의 화질
  * Model에 맞게 이미지 전처리 해주기
