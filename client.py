from typing import List
from statistics_logger.core import ExecutionTimesBaseStatistics
from statistics_logger.decorators import WithMeanStatisticsLogger, WithSummaryStatisticsLogger
from statistics_logger.functional_decorators import with_mean_statistics, with_summary_statistics

TEST_TIMES: List[float] = [0.15, 0.45, 0.20, 0.90, 0.30]

print("=== A. DEMO: Dekoratory Obiektowe (GoF) ===")

base_stats = ExecutionTimesBaseStatistics(TEST_TIMES)

combined_decorated = WithSummaryStatisticsLogger(
    WithMeanStatisticsLogger(base_stats)
)

print("\n--- Obiekt: Summary + Mean + Base ---")
combined_decorated.display_statistics()


print("\n=== B. DEMO: Dekoratory Funkcyjne (@) ===")

class DecoratedExecutionTimesStatistics(ExecutionTimesBaseStatistics):
    @with_summary_statistics
    @with_mean_statistics
    def display_statistics(self) -> None:
        super().display_statistics()

functional_stats = DecoratedExecutionTimesStatistics(TEST_TIMES)

print("\n--- Funkcyjne: Summary (@) + Mean (@) + Base ---")
functional_stats.display_statistics()

print("\nKoniec demonstracji.")
