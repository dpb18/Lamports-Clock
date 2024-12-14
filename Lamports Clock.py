class LamportClock:
    def __init__(self):
        self.time = 0

    def tick(self):
        """Increment the logical clock time for an internal event."""
        self.time += 1

    def update(self, received_time):
        """Update the logical clock with the maximum of its time and the received time."""
        self.time = max(self.time, received_time) + 1

    def get_time(self):
        """Return the current logical clock time."""
        return self.time

# Example usage in a distributed system
def process_A():
    clock_A = LamportClock()
    print(f"Process A starts with time {clock_A.get_time()}")

    # Event 1 at A
    clock_A.tick()
    print(f"Event 1 at A, time: {clock_A.get_time()}")

    # Send message to Process B
    message_time = clock_A.get_time()

    # Assume we now handle this in Process B
    process_B(message_time)

def process_B(received_time):
    clock_B = LamportClock()
    print(f"Process B starts with time {clock_B.get_time()}")

    # Receive message from A
    clock_B.update(received_time)
    print(f"Message received at B, updated time: {clock_B.get_time()}")

    # Event 2 at B
    clock_B.tick()
    print(f"Event 2 at B, time: {clock_B.get_time()}")

if __name__ == "__main__":
    process_A()
