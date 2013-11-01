#!/usr/bin/env perl

# Utility script to split a text file into one sentence per line.
# Usage: ./sentences2lines.pl > output.txt

my $file_to_split = 'sentences_but_not_one_per_line.txt';

use File::Slurp;
use Lingua::Sentence;

my $splitter = Lingua::Sentence->new("en");

my $text = read_file($file_to_split) ;
$text =~ s/\r|\n/ /g;

my @sentences = $splitter->split_array($text);

foreach my $sentence (@sentences) {
  my $len = length($sentence);
  # Print to stdout.
  print $sentence . "\n";
}


