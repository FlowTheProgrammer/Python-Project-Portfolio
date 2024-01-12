
names = []

with open('100 Days of Code Projects/Intermediate Projects/24. Mail Merge/Input/Names/name.txt') as file:
            for i in file.readlines():
                names.append(i.strip())    
            file.close()


for name in names:
        with open('100 Days of Code Projects\Intermediate Projects/24. Mail Merge\Input\Letters\starting_letter.txt') as file:
                file_content = file.read()
                file.close()
        with open(f"100 Days of Code Projects\Intermediate Projects/24. Mail Merge\Output\ReadyToSend/{name}'s_letter.txt'", mode='w') as file:
                old_text = "Dear [name],"
                new_text= f'Dear {name},'
                new_file = file_content.replace(old_text,new_text)
                file.write(new_file)