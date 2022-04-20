# dqn-atari-breakout/0_cartpole-v0

## 아나콘다 가상환경 만들기
conda create -n py37 python=3.7

## 가상환경 접속
conda activate py37

## 라이브러리 설치
pip install gym
pip install pygame

## 아나콘다 명령어 모음 (복붙용)
conda info --envs
conda env remove -n py37
conda create -n py37 python=3.7
conda activate py37
conda deactivate