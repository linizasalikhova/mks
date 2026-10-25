## запуск локально
cd 'C:\Projects\mks\fastapi\'
.\.venv\Scripts\Activate.ps1
deactivate
python -m uvicorn src.main:app --reload

## загрузка обновления на github
git status
git add .
git commit -m "privet"
git push origin main


## загрузка обновлений с github
ssh user@192.168.88.24
git pull
docker compose down
docker compose up -d --build