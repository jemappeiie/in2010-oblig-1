def main():
    N = int(input())
    set = SetHash()
    for _ in range(N):
        command = input().split()
        if command[0] == "contains":
            print(str(set.contains(int(command[1]))).lower())

        if command[0] == "insert":
            set.insert(int(command[1]))

        if command[0] == "remove":
            set.remove(int(command[1]))

        if command[0] == "size":
            print(set.size())


class SetHash:
    def __init__(self):
        self.buckets = [
            [] for _ in range(8)
        ]  # Added _resize() check if all buckets are filled
        self.uniq = 0

    def contains(self, value):
        index = value % len(self.buckets)
        return value in self.buckets[index]

    def insert(self, value):

        index = value % len(self.buckets)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)
            self.uniq += 1

            # resize check
            if self.uniq > len(self.buckets):
                self._resize()

    def remove(self, value):
        index = value % len(self.buckets)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)
            self.uniq -= 1

    def size(self):
        return self.uniq

    # Code passes testrunner without _resize() as well
    def _resize(self):
        old_buckets = self.buckets
        new_buckets = [[] for _ in range(len(old_buckets) * 2)]
        for bucket in old_buckets:
            for value in bucket:
                index = value % len(new_buckets)
                new_buckets[index].append(value)
        self.buckets = new_buckets


if __name__ == "__main__":
    main()
