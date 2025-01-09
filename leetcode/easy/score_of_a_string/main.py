class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_list = [ord(char) for char in s]
        sum = 0
        for i, char in enumerate(ascii_list):
            next_el_index = i + 1
            if next_el_index < len(ascii_list):
                sum += abs(char - ascii_list[next_el_index])

        return sum