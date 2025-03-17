def transform_lyrics_from_file(input_file, output_file):
    # Read the lyrics from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        lyrics = file.readlines()
    
    # Process the lyrics
    transformed_lyrics = []
    for line in lyrics:
        line = line.strip()  # Remove leading/trailing whitespace
        line = line.capitalize()  # Capitalize the first letter of each line
        if line:  # Ensure empty lines aren't added
            transformed_lyrics.append(line)
    
    # Write the transformed lyrics to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in transformed_lyrics:
            file.write(f"\"{line}\"" + ",\n")
    
    print(f"Transformed lyrics have been saved to {output_file}")

# Example usage
input_file = "lyrics/input_lyrics.txt"  
output_file = "lyrics/output_lyrics.txt"
transform_lyrics_from_file(input_file, output_file)
