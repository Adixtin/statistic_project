from typing import List
import statistics
from .core import IStatisticsLogger


def with_mean_statistics(func):
    def wrapper(self: IStatisticsLogger, *args, **kwargs):
        times = self.get_execution_times()
        if times:
            mean = statistics.mean(times)
            print("--- Added Mean Statistics (Functional) ---")
            print(f"Mean execution time: {mean:.4f}s")
            print("------------------------------------------")
        
        return func(self, *args, **kwargs)
        
    return wrapper


def with_summary_statistics(func):
    def wrapper(self: IStatisticsLogger, *args, **kwargs):
        times = self.get_execution_times()
        if times:
            count = len(times)
            total_sum = sum(times)
            min_val = min(times)
            max_val = max(times)
            
            print("--- Added Summary Statistics (Functional) ---")
            print(f"Total records (Count): {count}")
            print(f"Total sum of times (Sum): {total_sum:.4f}s")
            print(f"Minimum time (Min): {min_val:.4f}s")
            print(f"Maximum time (Max): {max_val:.4f}s")
            print("---------------------------------------------")
            
        return func(self, *args, **kwargs)
        
    return wrapper
