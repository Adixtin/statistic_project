from __future__ import annotations
from typing import List, Protocol

class IStatisticsLogger(Protocol):
    def display_statistics(self) -> None:
        ...
        
    def get_execution_times(self) -> List[float]:
        ...

class StatisticsLogger(IStatisticsLogger):
    def display_statistics(self) -> None:
        raise NotImplementedError("Subclass must implement abstract method")
        
    def get_execution_times(self) -> List[float]:
        raise NotImplementedError("Subclass must implement abstract method")


class ExecutionTimesBaseStatistics(StatisticsLogger):
    def __init__(self, execution_times: List[float]):
        if not all(isinstance(t, (int, float)) for t in execution_times):
             raise TypeError("All execution times must be numeric (int or float).")
        self.execution_times: List[float] = execution_times
        self._last_breakdown_times: List[float] = []

    def get_execution_times(self) -> List[float]:
        return self.execution_times

    def display_statistics(self) -> None:
        print("--- Execution Times ---")
        for time in self.execution_times:
            print(f"Result: {time:.4f}s")
        print("-----------------------")

    def __str__(self) -> str:
        return f"ExecutionTimesBaseStatistics(count={len(self.execution_times)})"
