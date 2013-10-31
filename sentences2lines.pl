#!/usr/bin/env perl

# Utility script to split a text file into one sentence per line.
# Usage: ./sentences2lines.pl > output.txt

my $file_to_split = 'data.txt';

use File::Slurp;
use Lingua::Sentence;

my $splitter = Lingua::Sentence->new("en");

my $text = read_file($file_to_split) ;
$text =~ s/\r|\n/ /g;

my @sentences = $splitter->split_array($text);

foreach my $sentence (@sentences) {
  $len = length($sentence);
  # Print to stdout.
  print $sentence . "\n";
}


