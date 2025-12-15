from functions import get_file_content
print(f'Result:\n{get_file_content.get_file_content('calculator', 'lorem.txt')}')
print(f'Result:\n{get_file_content.get_file_content('calculator', 'main.py')}')
print(f'Result:\n{get_file_content.get_file_content('calculator', 'pkg/calculator.py')}')
print(f'Result:\n{get_file_content.get_file_content('calculator', '/bin')}')
print(f'Result:\n{get_file_content.get_file_content('calculator', '../')}')