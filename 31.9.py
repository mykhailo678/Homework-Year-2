import numpy as np
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def run_simulation(N, m, t, t1):
    arrival_times = np.sort(np.random.uniform(-t, 0, N))
    turnstiles = np.full(m, -t, dtype=float)
    wait_durations = np.zeros(N)

    for i in range(N):
        arrival = arrival_times[i]
        idx = np.argmin(turnstiles)
        start_service = max(arrival, turnstiles[idx])
        service_duration = np.random.uniform(1/60, t1)
        turnstiles[idx] = start_service + service_duration
        wait_durations[i] = turnstiles[idx] - arrival

    return wait_durations

def main():
    N, m, t, t1 = 5000, 10, 60, 0.5
    num_simulations = 200
    all_results = []

    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = [executor.submit(run_simulation, N, m, t, t1) for _ in range(num_simulations)]
        for future in futures:
            all_results.extend(future.result())

    required_time = np.percentile(all_results, 90)
    print(f"{required_time:.2f}")

if __name__ == "__main__":
    main()