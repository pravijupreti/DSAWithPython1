class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}
        
        # Build the word frequency map
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        n = len(s)
        result = []
        
        # Iterate over all possible starting points modulo word_len
        for i in range(word_len):
            left = i
            right = i
            seen = {}
            count = 0
            
            while right + word_len <= n:
                # Extract a word from the window
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                    # If word is seen too many times, adjust the window
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If the window contains all words, record the start index
                    if count == num_words:
                        result.append(left)
                else:
                    # Reset the window if an invalid word is found
                    seen.clear()
                    count = 0
                    left = right
        
        return result
