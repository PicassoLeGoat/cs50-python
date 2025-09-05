# Ask the user for a file name
filename = input("File name: ").strip()  # strip removes extra spaces

# Convert to lowercase to make checking case-insensitive
filename_lower = filename.lower()

# Check the file extension and print media type
if filename_lower.endswith(".gif"):
    print("image/gif")
elif filename_lower.endswith(".jpg") or filename_lower.endswith(".jpeg"):
    print("image/jpeg")
elif filename_lower.endswith(".png"):
    print("image/png")
elif filename_lower.endswith(".pdf"):
    print("application/pdf")
elif filename_lower.endswith(".txt"):
    print("text/plain")
elif filename_lower.endswith(".zip"):
    print("application/zip")
else:
    # Unknown extension or no extension
    print("application/octet-stream")
