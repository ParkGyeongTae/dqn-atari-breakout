# dqn-atari-breakout/0_cartpole-v0

## 사용방법

### Step 1) 아나콘다 가상환경 만들기
conda create -n py37 python=3.7

### Step 2) 가상환경 접속
conda activate py37

### Step 3) 라이브러리 설치
pip install gym==0.23.1
pip install pygame==2.1.2

### Step 4) 파일 실행
example) python 0_cartpole-v0-example.py
example) python 1_cartpole-v0-first-observation.py
...

### (참고) 아나콘다 명령어 모음 (복사 붙여넣기 용도)
conda info --envs
conda env remove -n py37
conda create -n py37 python=3.7
conda activate py37
conda deactivate