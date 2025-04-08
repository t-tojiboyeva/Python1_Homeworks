import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

def threaded_prime_checker(start_range, end_range, num_threads=4):
    threads = []
    primes = []
    results = [[] for _ in range(num_threads)]
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i < num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes, args=(start, end, results[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for sublist in results:
        primes.extend(sublist)

    print("Primes:", sorted(primes))


threaded_prime_checker(10, 100, num_threads=4)




import threading
from collections import defaultdict
import os

def count_words(lines, word_count):
    for line in lines:
        words = line.strip().split()
        for word in words:
            cleaned_word = word.lower().strip(",.!?;:\"'()[]")
            if cleaned_word:
                word_count[cleaned_word] += 1

def threaded_file_processing(filename, num_threads=4):
    if not os.path.exists(filename):
        print("File not found.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads
    threads = []
    results = [defaultdict(int) for _ in range(num_threads)]

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else total_lines
        thread = threading.Thread(target=count_words, args=(lines[start:end], results[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_counts = defaultdict(int)
    for result in results:
        for word, count in result.items():
            final_counts[word] += count

    
    sorted_words = sorted(final_counts.items(), key=lambda x: x[1], reverse=True)
    print("Top 10 most common words:")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")



