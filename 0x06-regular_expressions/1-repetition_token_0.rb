#!/usr/bin/env ruby

# Ensure there is an argument provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern to match the word "School"
pattern = /hbt{2,5}n/

# Perform the regex scan on the input string
matches = input_string.scan(pattern)

# Output the matched results, if any
puts matches.join("\n")
