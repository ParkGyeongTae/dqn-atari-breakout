# dqn-atari-breakout

# 아나콘다 가상환경 만들기
conda create -n py37 python=3.7

# 가상환경 접속
conda activate py37

# 라이브러리 설치
conda install -c conda-forge gym
conda install -c cogsci pygame
pip install gym[all]






conda info --envs
conda env remove -n py36
conda create -n py36 python=3.6
conda activate py36
conda deactivate