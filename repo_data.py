import requests
import json
import base64
import argparse
import os

SAVE = "static/projects"

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_repo_data(owner, repo_name):
    create_folder(SAVE)
    url = f'https://api.github.com/repos/{owner}/{repo_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        repo_data = {
            'name': data.get('name', ''),
            'about': data.get('description', ''),
            'url': data.get('html_url', ''),
            'homepage': data.get('homepage', ''),
        }

        # Запрос для получения README
        readme_url = f'https://api.github.com/repos/{owner}/{repo_name}/readme'
        readme_response = requests.get(readme_url)
        if readme_response.status_code == 200:
            readme_data = readme_response.json()
            readme_content = base64.b64decode(readme_data['content']).decode('utf-8')
            repo_data['readme'] = readme_content
        else:
            repo_data['readme'] = 'README не найден.'

        # Сохраняем данные в файл
        with open(f'{SAVE}/{repo_name}.json', 'w', encoding='utf-8') as f:
            json.dump(repo_data, f, ensure_ascii=False, indent=4)
        
        print(f"Данные {repo_name} сохранены!")
    else:
        print(f"Ошибка при запросе к GitHub API: {response.status_code}")


parser = argparse.ArgumentParser(description='Получение данных о репозитории с GitHub')
parser.add_argument('repo_name', type=str, help='Название репозитория на GitHub')
args = parser.parse_args()
owner = "falbue"
get_repo_data(owner, args.repo_name)