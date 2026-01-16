#!/usr/bin/env python3
para = input("Enter a paragraph to filter out unique words:\n").lower()
def word_filter(a):
	words = a.split()
	ignore = {"a", "an", "the", "and", "or", "but", "if", "then", "else", "when", "at", "by", "for", "in",
          	"of", "on", "to", "with", "from", "up", "down", "as", "is", "are", "was", "were", "be",
          	"been", "being", "have", "has", "had", "do", "does", "did", "will", "would", "can", "could",
          	"should", "may", "might", "must", "i", "me", "my", "you", "your", "he", "his", "she", "her",
          	"it", "its", "we", "us", "our", "they", "them", "their", "this", "that", "these", "those",
          	"am", "so", "no", "not", "too", "very", "just", "over", "under", "again", "once", "why"}

	unique = {word.strip(".!,?{};:-_()''") for word in words if word not in ignore}
	print("List of unique words: ")
	for num, word in enumerate(unique, start=1):
		print(f"{num}. {word}")
	print("\nTotal unique words:", len(unique))
word_filter(para)


