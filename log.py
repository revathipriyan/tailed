import time

log_file_path = "dummy_log.txt"
with open(log_file_path, 'a') as dummy_log:
    counter = 1
    while True:
        dummy_log.write(f"Log entry {counter}\n")
        dummy_log.flush()  # Flush the buffer to ensure the line is written immediately
        counter += 1
        time.sleep(2)  