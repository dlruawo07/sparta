class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1
    
    # percolate: 스며들다
    def _percolate_up(self):
        # 가장 최근에 추가된 요소
        current = len(self)

        # left라면 2*current, right라면 2*current+1 이므로 parent는 항상 current//2
        parent = current // 2

        # parent와 비교했을 때 parent보다 크다면 swap
        while parent > 0:
            # if self.items[current] < self.items[parent]: # ===> min_heap
            if self.items[current] > self.items[parent]:
                self.items[current], self.items[parent] = self.items[parent], self.items[current]

            # 비교가 끝날 때마다 current는 한 칸씩 위로 올라감
            current = parent
            # parent도 마찬가지로 한 칸씩 올라감
            parent = current // 2

    def _percolate_down(self, current):
        biggest = current
        left = 2 * current
        right = 2 * current + 1

        # left가 self의 범위 안에 있고 items의 left번째 요소가 biggest번째 요소보다 크다면 biggest에 left 저장
        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        # right가 self의 범위 안에 있고 items의 right번째 요소가 biggest번째 요소보다 크다면 biggest에 right 저장
        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        # 위 두 if문에서 biggest가 바뀌었다면 current번째 요소와 biggest번째 요소 swap
        if biggest != current:
            self.items[current], self.items[biggest] = self.items[biggest], self.items[current]
            # current를 biggest 기준으로 무한 반복 (언제까지? current가 biggest일 때까지)
            self._percolate_down(biggest)


    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None
        
        # 0번째는 None이기 때문에 그 다음 번째인 1이 root
        root = self.items[1]
        # 마지막 요소를 맨 앞으로 가져옴 
        # (원래는 둘이 swap 해야 하는데 어차피 마지막 요소는 바로 pop할거라 굳이 1번째 요소를 마지막에 넣어줄 필요가 없음)
        self.items[1] = self.items[-1]
        # 마지막 요소 제거
        self.items.pop()
        # 힙 수정
        self._percolate_down(1)

        return root