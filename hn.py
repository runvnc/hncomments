import requests
import json

def get_user_comments(username, output_file):
    user_url = f'https://hacker-news.firebaseio.com/v0/user/{username}.json'
    print(f'Fetching data for user {username}...')
    user_data = requests.get(user_url).json()
    print(f'Finished fetching data for user {username}.')

    if not user_data or 'submitted' not in user_data:
        print(f'No data found for user {username}')
        return

    with open(output_file, 'a') as f:
        ln = len(user_data['submitted'])
        n = 0
        for item_id in user_data['submitted']:
            n += 1
            item_url = f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'
            print(f'Fetching item {item_id} #{n} of {ln}...')
            item_data = requests.get(item_url).json()
            print(f'Finished fetching item {item_id}.')
            if item_data and item_data.get('type') == 'comment':
                f.write(json.dumps(item_data) + '\n')



if __name__ == "__main__":
    username = 'ilaksh'
    print(f'Starting process for user {username}...')
    output_file = f'{username}_comments.jsonl'
    get_user_comments(username, output_file)
    print(f'Comments are being saved incrementally to {output_file}')
    print(f'Process completed for user {username}.')

