### Exercices ###

# 1 - Write a function which generates a six digit/character random_user_id.
import random
import string

def generate_random_user_id():
    random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return random_id

random_user_id = generate_random_user_id()
print("Random User ID:", random_user_id)
# 2 - Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    try:
        char_count = int(input("Enter the number of characters for each user ID: "))
        id_count = int(input("Enter the number of user IDs to generate: "))

        if char_count <= 0:
            print("Error: Number of characters should be greater than 0.")
            return

        user_ids = []
        for _ in range(id_count):
            random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=char_count))
            user_ids.append(random_id)

        return user_ids

    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

generated_user_ids = user_id_gen_by_user()

if generated_user_ids:
    print("Generated User IDs:", generated_user_ids)
# 3 - Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return red, green, blue

generated_color = rgb_color_gen()
print("Generated RGB Color:", generated_color)

#============================================================================
#Level 2
#============================================================================

# 1 - Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    hex_chars = "0123456789ABCDEF"

    hex_colors = []
    for _ in range(num_colors):
        color = "#" + ''.join(random.choice(hex_chars) for _ in range(6))
        hex_colors.append(color)

    return hex_colors

num_colors_to_generate = 5
generated_hex_colors = list_of_hexa_colors(num_colors_to_generate)
print("Generated Hexadecimal Colors:", generated_hex_colors)
# 2 - Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        rgb_colors.append((red, green, blue))

    return rgb_colors

num_colors_to_generate = 5
generated_rgb_colors = list_of_rgb_colors(num_colors_to_generate)
print("Generated RGB Colors:", generated_rgb_colors)
# 3 - Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(color_type, num_colors):
    if color_type.lower() == "hex":
        return list_of_hexa_colors(num_colors)
    elif color_type.lower() == "rgb":
        return list_of_rgb_colors(num_colors)
    else:
        print("Invalid color type. Supported types: 'hex' or 'rgb'")
        return None

#=============================================================================
#Level 3
#=============================================================================

# 1 - Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(input_list):
    shuffled_list = input_list.copy()

    random.shuffle(shuffled_list)
    
    return shuffled_list

original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)

print("Original List:", original_list)
print("Shuffled List:", shuffled_result)
# 2 - Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def seven_unique_random_numbers():
    unique_numbers = random.sample(range(10), 7)
    
    return unique_numbers

random_numbers = seven_unique_random_numbers()
print("Seven Unique Random Numbers:", random_numbers)