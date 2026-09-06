class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded_piece = str(len(s)) + "!" + s
            encoded += encoded_piece
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            index = s.find("!", i)
            length = s[i:index]
            i_len = int(length)
            start = index + 1
            end = start + i_len
            decoded_piece = s[start:end]
            decoded.append(decoded_piece)
            i = end
        return decoded