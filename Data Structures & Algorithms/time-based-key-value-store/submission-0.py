class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([timestamp, value])

    def get(self, key, target_time):
      
        if key not in self.store:
            return ""
            
        values_list = self.store[key]
        
        left = 0
        right = len(values_list) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            
           
            time_at_mid = values_list[mid][0]
            value_at_mid = values_list[mid][1]
            
            if time_at_mid <= target_time:
             
                res = value_at_mid
             
                left = mid + 1
            else:
                right = mid - 1
                
        return res
                    



       


        
