from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Convert list to a set for O(1) lookups
        word_set = set(wordList)
        
        # If the destination word isn't even in the dictionary, no path can exist
        if endWord not in word_set:
            return 0
            
        # The queue stores tuples of (current_word, path_length)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            
            # If we reached our destination, return the total words in the path
            if word == endWord:
                return steps
                
            # Try mutating every single character slot of the word
            word_chars = list(word)
            for i in range(len(word_chars)):
                original_char = word_chars[i]
                
                # Swap out the character for all 26 possible letters
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                        
                    word_chars[i] = c
                    next_word = "".join(word_chars)
                    
                    # If the mutated word is valid, explore it next
                    if next_word in word_set:
                        queue.append((next_word, steps + 1))
                        # Remove it from the set to avoid redundant visits
                        word_set.remove(next_word)
                        
                # Restore the original character before moving to the next index slot
                word_chars[i] = original_char
                
        return 0