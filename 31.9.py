import random
import statistics


class StadiumSimulation:
    def __init__(self, N, m, t1, t_open):
        self.N = N
        self.m = m
        self.t1 = t1
        self.t_open = t_open * 60

    def run_simulation(self):
        arrivals = [random.uniform(0, self.t_open) for _ in range(self.N)]
        arrivals.sort()

        turnstiles = [0.0] * self.m
        total_delays = []

        for arrival_time in arrivals:
            idx = turnstiles.index(min(turnstiles))
            start_service = max(arrival_time, turnstiles[idx])

            wait_time = start_service - arrival_time
            service_time = random.uniform(1, self.t1)

            turnstiles[idx] = start_service + service_time
            total_delays.append(wait_time + service_time)

        return total_delays


def perform_analysis():
    N = 10000
    m = 9
    t1 = 10
    t_open = 90
    iterations = 100

    all_p90_thresholds = []

    for _ in range(iterations):
        sim = StadiumSimulation(N, m, t1, t_open)
        delays = sim.run_simulation()
        delays.sort()
        all_p90_thresholds.append(delays[int(0.9 * len(delays)) - 1])

    avg_p90 = statistics.mean(all_p90_thresholds)

    print(f"N: {N}, m: {m}, t1: {t1}, t_open: {t_open}")
    print(f"90% probability delay: {avg_p90:.2f} sec")
    print(f"Recommended arrival time: {avg_p90 / 60:.2f} min before start")


if __name__ == "__main__":
    perform_analysis()
