import time
import matplotlib.pyplot as plt
from recommender.recommender import Recommender

def benchmark_recommender():
    num_users_list = [10, 50, 100, 500, 1000]
    retrieval_times = []

    for num_users in num_users_list:
        rec = Recommender(num_users=num_users, num_items=500)
        # Add random interactions
        for u in range(num_users):
            for i in range(50):
                rec.add_interaction(u, np.random.randint(0, 500), np.random.randint(1, 6))
        # Measure retrieval time
        start = time.time()
        for u in range(num_users):
            rec.get_top_k_recommendations(u, k=5)
        end = time.time()
        avg_time = (end - start) / num_users
        retrieval_times.append(avg_time)

    # Plot results
    plt.figure(figsize=(8,5))
    plt.plot(num_users_list, retrieval_times, marker='o')
    plt.title("Average Recommendation Retrieval Time vs Number of Users")
    plt.xlabel("Number of Users")
    plt.ylabel("Average Time per User (s)")
    plt.grid(True)
    plt.savefig("retrieval_time_plot.png")
    plt.show()

if __name__ == "__main__":
    import numpy as np
    benchmark_recommender()
