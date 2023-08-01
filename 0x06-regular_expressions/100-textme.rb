#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*9)\] \[to:(.*9)\] \[flags:(.*9)\]/).join(",") 
