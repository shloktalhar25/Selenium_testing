from concurrent.futures import ThreadPoolExecutor
from worker import run_user


with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []

    for _ in range(10):
        futures.append(
            executor.submit(run_user)
        )

    results = [f.result() for f in futures]

    # Calculate Metrics
    total_users = len(results)
    successful_users = sum(r["success"] for r in results)
    failed_users = total_users - successful_users

    total_time = sum(r["execution_time"] for r in results)
    average_time = total_time / total_users if total_users > 0 else 0

    # Display Results
    print("\n" + "="*40)
    print(f"TOTAL USERS: {total_users}")
    print(f"SUCCESSFUL:  {successful_users}")
    print(f"FAILED:      {failed_users}")
    print(f"AVG TIME:    {average_time:.2f}s")
    print("="*40 + "\n")



