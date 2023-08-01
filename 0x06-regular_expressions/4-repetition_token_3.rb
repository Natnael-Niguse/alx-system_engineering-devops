#!/usr/bin/env ruby

# Ensure there is an argument provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern to match "t" with 2 to 5 repetitions between "h" and "n"
pattern = /hbt*n/

# Perform the regex scan on the input string
matches = input_string.scan(pattern)

# Output the matched results, if any, on separate lines
puts matches.join("\n")
