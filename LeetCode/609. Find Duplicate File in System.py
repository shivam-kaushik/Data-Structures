class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_files = defaultdict(list)
    
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]
                full_path = directory + '/' + file_name
                content_to_files[content].append(full_path)
        
        duplicates = [group for group in content_to_files.values() if len(group) > 1]
        
        return duplicates