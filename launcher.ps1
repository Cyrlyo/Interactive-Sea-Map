.venv/Scripts/activate
echo "Try to open the map in your browser..."
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" "http://127.0.0.1:8000"
# start chrome "http://localhost:8000"
uvicorn app:app