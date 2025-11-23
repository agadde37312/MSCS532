import time
import matplotlib.pyplot as plt
import numpy as np
from recommender.recommender import Recommender
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def benchmark_recommender():
    """
    Benchmarks the recommender system for different numbers of users,
    measuring average top-k retrieval time per user.
    """
    num_users_list = [10, 50, 100, 500, 1000]
    retrieval_times = []

    num_items = 500
    k = 5

    for num_users in num_users_list:
        logging.info(f"Benchmarking with {num_users} users...")
        rec = Recommender(num_users=num_users, num_items=num_items, embedding_dim=32)

        # Add random interactions
        for u in range(num_users):
            for _ in range(50):
                item_id = np.random.randint(0, num_items)
                rating = np.random.randint(1, 6)
                rec.add_interaction(u, item_id, rating)

        # Measure retrieval time for all users
        start_time = time.time()
        for u in range(num_users):
            rec.get_top_k_recommendations(u, k=k)
        end_time = time.time()

        avg_time = (end_time - start_time) / num_users
        retrieval_times.append(avg_time)
        logging.info(f"Avg retrieval time per user: {avg_time:.6f} seconds")

    # Plot results
    plt.figure(figsize=(8,5))
    plt.plot(num_users_list, retrieval_times, marker='o', linestyle='-', color='blue')
    plt.title("Average Recommendation Retrieval Time vs Number of Users")
    plt.xlabel("Number of Users")
    plt.ylabel(f"Average Time per User (s) [Top-{k} Recommendations]")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("retrieval_time_plot.png")
    plt.show()

if __name__ == "__main__":
    benchmark_recommender()
