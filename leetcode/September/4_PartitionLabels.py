class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_last_pos = {}
        
        for idx, char in enumerate(S):            
            char_last_pos[char] = idx
            
        start, partition_length = 0, []
        last_position = 0
        
        for idx, char in enumerate(S):
            last_position = max(last_position, char_last_pos[char])
            if idx == last_position:
                cur_partition_length = last_position - start + 1
                partition_length.append( cur_partition_length )
                start = idx + 1
        return partition_length