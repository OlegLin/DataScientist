def create_file_with_numbers(n, file_name) -> None:
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(n):
        file.write(f'{i} \n')
    file.close()

create_file_with_numbers(7, 'range_[number].txt')