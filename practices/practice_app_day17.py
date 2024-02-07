#Python Carnival Costume Extravaganza
def add_costume(costumes, name, theme, accessories):
    try:
        if not theme:
            raise ValueError("A costume must have a theme.")

        costume_details = {'name': name, 'theme': theme, 'accessories': accessories}
        costumes.append(costume_details)
        print(f"🎉 Costume '{name}' added successfully for the '{theme}' theme with accessories: {accessories}!")

    except ValueError as ve:
        print(f"🚨 Error: {ve}")
    except Exception as e:
        print(f"🎭 An unexpected error occurred: {e}")

def display_costumes(costumes):
    try:
        if not costumes:
            raise ValueError("No costumes to display. The carnival needs more flair!")

        print("🎭 Carnival Costume Extravaganza:")
        for index, costume in enumerate(costumes, start=1):
            accessories = ', '.join(costume['accessories']) if 'accessories' in costume else 'None'
            print(f"{index}. {costume['name']} - Theme: {costume['theme']} - Accessories: {accessories}")

    except ValueError as ve:
        print(f"🚨 Error: {ve}")
    except Exception as e:
        print(f"🎭 An unexpected error occurred: {e}")

def main():
    costumes = []

    # Adding costumes with packing
    add_costume(costumes, "Star Performer", "Galactic Glam", ["Sparkling Wand", "Shining Crown"])
    add_costume(costumes, "Safari Explorer", "Wild Safari", ["Explorer Hat", "Binoculars"])
    add_costume(costumes, "Mystery Magician", "", [])  # Oops, someone forgot the theme!

    # Displaying costumes with unpacking and zip
    display_costumes(costumes)

if __name__ == "__main__":
    main()