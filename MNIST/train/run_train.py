import subprocess

batch_sizes = [1, 4, 16, 64, 256]
worker_nums = [1, 2, 3, 4]

for batch_size in batch_sizes:
    for num_workers in worker_nums:
        subprocess.run(['python3', 'train_local.py', str(num_workers), str(batch_size)])

for batch_size in batch_sizes:
    for num_workers in worker_nums:
        subprocess.run(['python3', 'train_redis.py', str(num_workers), str(batch_size)])