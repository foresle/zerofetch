source ./venv/bin/activate
pip install -r ./requirements.txt
python -m nuitka --follow-imports main.py
sudo cp main.bin /bin/zerofetch