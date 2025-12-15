from __future__ import annotations
from typing import List
import statistics
from .core import IStatisticsLogger


class StatisticsLoggerDecorator(IStatisticsLogger):
    def __init__(self, logger: IStatisticsLogger):
        self._logger = logger

    def display_statistics(self) -> None:
        self._logger.display_statistics()

    def get_execution_times(self) -> List[float]:
        return self._logger.get_execution_times()


class WithMeanStatisticsLogger(StatisticsLoggerDecorator):
    def display_statistics(self) -> None:
        times = self.get_execution_times()
        if times:
            mean = statistics.mean(times)
            print("--- Added Mean Statistics ---")
            print(f"Mean execution time: {mean:.4f}s")
            print("-----------------------------")
        super().display_statistics() 

class WithSummaryStatisticsLogger(StatisticsLoggerDecorator):
    def display_statistics(self) -> None:
        times = self.get_execution_times()
        if times:
            count = len(times)
            total_sum = sum(times)
            min_val = min(times)
            max_val = max(times)
            
            print("--- Added Summary Statistics ---")
            print(f"Total records (Count): {count}")
            print(f"Total sum of times (Sum): {total_sum:.4f}s")
            print(f"Minimum time (Min): {min_val:.4f}s")
            print(f"Maximum time (Max): {max_val:.4f}s")
            print("--------------------------------")
            
        super().display_statistics()
