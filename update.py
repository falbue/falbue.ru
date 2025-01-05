import requests
import os
import sys
import config

GITHUB_API_URL = "https://api.github.com"
ACCESS_TOKEN = config.TOKEN_GITHUB
repo_owner = config.OWNER
PATH = config.PATH_UPDATE

def is_repo_private(repo_owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}"
    headers = {
        "Authorization": f"token {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo_data = response.json()
        return repo_data.get("private", False)
    else:
        print(f"Ошибка при проверке репозитория: {response.status_code}")
        return None

def get_contents(repo_owner, repo_name, path="", use_token=False):
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/contents/{path}"
    headers = {}
    if use_token:
        headers["Authorization"] = f"token {ACCESS_TOKEN}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при получении содержимого: {response.status_code}")
        return None

def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_files(contents, repo_owner, repo_name, base_path="", use_token=False):
    for item in contents:
        if item['type'] == 'file':
            file_path = os.path.join(base_path, item['name'])
            download_file(item['download_url'], file_path, use_token)
        elif item['type'] == 'dir':
            dir_path = f"{os.path.join(base_path, item['name'])}"
            create_dir_if_not_exists(dir_path)
            sub_contents = get_contents(repo_owner, repo_name, item['path'], use_token)
            if sub_contents:
                download_files(sub_contents, repo_owner, repo_name, base_path=os.path.join(base_path, item['name']), use_token=use_token)

def download_file(file_url, file_path, use_token=False):
    headers = {}
    if use_token:
        headers["Authorization"] = f"token {ACCESS_TOKEN}"
    
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        with open(f"{file_path}", 'wb') as f:  # Сохраняем в бинарном режиме
            f.write(response.content)
        print(f"Файл {file_path} успешно скачан и сохранён.")
    else:
        print(f"Ошибка при скачивании {file_path}: {response.status_code}")

def update_repo(repo_name):
    print(f"Обновление репозитория {repo_owner}/{repo_name}...")
    repo_private = is_repo_private(repo_owner, repo_name)
    if repo_private is None:
        return  # Прерывание выполнения в случае ошибки проверки репозитория
    
    use_token = repo_private  # Используем токен только для приватного репозитория
    contents = get_contents(repo_owner, repo_name, use_token=use_token)
    save_path = f"{PATH}{repo_name}"
    if contents:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        download_files(contents, repo_owner, repo_name, base_path=save_path, use_token=use_token)
    else:
        print("Не удалось получить содержимое репозитория.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python update.py <репозиторий>")
        sys.exit(1)

    repo_name = sys.argv[1]
    update_repo(repo_name)