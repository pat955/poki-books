#!/bin/bash

# Directory containing the zip files
DIR="release"

# Output file for checksums
CHECKSUM_FILE="checksums.txt"

# Create or clear the checksum file
: > "$CHECKSUM_FILE"

# Find all zip files in the specified directory and its subdirectories
find "$DIR" -type f | while read -r zipfile; do
    # Calculate checksum for each zip file
    checksum=$(sha256sum "$zipfile" | awk '{print $1}')
    # Get the relative path of the zip file for the output
    relative_path=$(realpath --relative-to="$DIR" "$zipfile")
    # Write the checksum and filename to the output file
    echo "$checksum  $relative_path" >> "$CHECKSUM_FILE"
done

echo "Checksums have been written to $CHECKSUM_FILE."
