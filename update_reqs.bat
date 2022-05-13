call venv\scripts\activate.bat
pip freeze > requirements.txt
git commit -m "Update requirements" requirements.txt
git push
echo "Updated requirements.txt and pushed it to Git"