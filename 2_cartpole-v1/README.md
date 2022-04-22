# dqn-atari-breakout/0_cartpole-v0

## 사용방법

### Step 1) 아나콘다 가상환경 만들기

conda create -n py37 python=3.7

### Step 2) 가상환경 접속

conda activate py37

### Step 3) 라이브러리 설치

pip install gym==0.23.1
pip install pygame==2.1.2
pip install keras==2.8.0
pip install tensorflow==2.8.0

### Step 4) 파일 실행

python 0_cartpole-v0-example.py
python 1_cartpole-v0-first-observation.py
...

### (참고) 아나콘다 명령어 모음 (복사 붙여넣기 용도)

1. 가상환경 리스트 확인 : conda info --envs
2. 가상환경 만들기     : conda create -n py37 python=3.7
3. 가상환경 지우기     : conda env remove -n py37
4. 가상환경 접속      : conda activate py37
5. 가상환경 종료      : conda deactivate