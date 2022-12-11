# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):  
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode
     
file_input_encode = open('input_data_encode.txt', 'r', encoding ='utf-8')
text_encode = file_input_encode.read()
file_input_encode.close()
result_encode = rle_encode(text_encode)
file_output_encode = open('output_data_encode.txt', 'w', encoding ='utf-8')
file_output_encode.write(result_encode)
file_output_encode.close()
print(result_encode)

file_input_decode = open('input_data_decode.txt', 'r', encoding ='utf-8')
text_decode = file_input_decode.read()
file_input_decode.close()
result_decode = rle_decode(text_decode)
file_output_decode = open('output_data_decode.txt', 'w', encoding ='utf-8')
file_output_decode.write(result_decode)
file_output_decode.close()
print(result_decode)
