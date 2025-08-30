def process_file():
    # Ask user for filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Process content
        word_count = len(content.split())
        uppercase_content = content.upper()

        # Write to new file
        with open("output.txt", "w") as output_file:
            output_file.write("MODIFIED CONTENT:\n")
            output_file.write(uppercase_content + "\n")
            output_file.write(f"WORD COUNT: {word_count}\n")

        print("🎉 Success! Processed content written to output.txt.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("⚠️ Error: Could not read the file. Make sure it's accessible and not locked.")
    except Exception as e:
        print(f"💥 Unexpected error: {e}")

# Run the program
process_file()