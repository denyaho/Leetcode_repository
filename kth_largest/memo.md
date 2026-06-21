# 問題
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


# Step1

* ヒープを使うとあったが、pythonでヒープをどう使うかわからなかったので、まずは解くことだけに専念

* 単純極まりないが、やったこととしては事前に配列をソートし、addメソッド呼び出し時の新たな要素は配列に入れつつ、再度ソートを行う。
  addの度にソートの時間計算量がO(nlogn)であるので、先にソートして、addする際には、二分探索をして適切な位置にinsertするアルゴリズム(O(logn) + O(n))の方が時間計算量は短くなる

* 他に考えたことは、ヒープソートを用いてソートした後に、最小の値をpopしていき値の取得、でpopした値は戻す。
　効率的ではなさそうで実装までは至らず　



```
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_largest = k
        self.sort_list = nums

    def add(self, val: int) -> int:
        self.sort_list.append(val)
        self.sort_list.sort(reverse=True)
        return self.sort_list[self.kth_largest - 1]
```




# step2

* 他の人のコードでは、K番目に大きい数を取得するためにmin-heapを用いている。
　heapでは、一番小さい数(min-heap)や一番大きい数(max-heap)を取得できるが、何番目に大きいといった情報は通常取得できない。
　そのため、min-heapとして値を保持する大きさをKで留め、サイズKを超えるようであれば最小値を取り出していく形を取る

* 参考資料
Quick Sortの常識
https://discord.com/channels/1084280443945353267/1200089668901937312/1203725416645271582




以下コードをディスコードより参照
https://discord.com/channels/1084280443945353267/1195700948786491403/1198906989070258277
```
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.hepify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

https://github.com/hayashi-ay/leetcode/blob/hayashi-ay-patch-43/703.%20Kth%20Largest%20Element%20in%20a%20Stream.md
```
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
```


https://github.com/kazukiii/leetcode/blob/arai60/kth-largest-element-in-a-stream/arai60/kth-largest-element-in-a-stream/step3.py
```
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.num_min_heap = []
        for num in nums:
            if len(self.num_min_heap) < k:
                heapq.heappush(self.num_min_heap, num)
            else:
                heapq.heappushpop(self.num_min_heap, num)

    def add(self, val: int) -> int:
        if len(self.num_min_heap) < self.k:
            heapq.heappush(self.num_min_heap, val)
        else:
            heapq.heappushpop(self.num_min_heap, val)
        return self.num_min_heap[0]

```

https://github.com/katataku/leetcode/blob/703.-Kth-Largest-Element-in-a-Stream/703.%20Kth%20Largest%20Element%20in%20a%20Stream.md
```
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._kth_largest_nums = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self._kth_largest_nums, val)
        if len(self._kth_largest_nums) > self._k:
            heappop(self._kth_largest_nums)
        return self._kth_largest_nums[0]
```

* Pythonのソートについて
　https://docs.python.org/3/howto/sorting.html

# 参考レビュ


https://github.com/ichika0615/arai60/pull/8#discussion_r1898337850
```
時間計算量からおおよその処理時間を推定することもできます。時間計算量の式に n の最大値を代入すると、おおよその計算ステップ数になります。この計算ステップ数を、各言語ごとの 1 秒あたりに処理可能な計算ステップ数で割ると、おおよその処理時間が出ます。
Python の場合は 1 秒あたり 100 万ステップ程度計算できます。この数字は、 CPU の動作周波数と、 1 クロック当たりの命令実行数、言語ごとの差から推定できます。 CPU の動作周波数は、最近のものですと、数 GHz = 数十億ヘルツになります。仮に 1 クロックに 1 命令実行できると仮定すると、 1 秒間に数十憶命令実行できます。また、 C/C++ といったオーバーヘッドの少ない言語ですと、 1 秒間に 1 ～ 10 億ステップ程度実行できます。 Python の場合、インタープリターのオーバーヘッドが大きいため、 1 秒間に 100 万ステップ程度処理できます。言語ごとの処理速度の差については、以下のページが参考になると思います。

https://github.com/niklas-heer/speed-comparison
https://benchmarksgame-team.pages.debian.net/benchmarksgame/box-plot-summary-charts.html
今回の場合は add() の処理時間が支配的です。 add() 1 回あたりの時間計算量は O(n log n) で、最大で 104 回呼ばれます。よって 10^4 * log 10^4 * 10^4 = 1.5 * 10^9 ステップくらいになると思います。 Python は 1 秒に 100 万ステップ = 1.0 * 10^6 ステップ程度処理できますので、 1.5 * 10^9 / 10^6 = 1.5 * 10^3 = 1500 秒程度かかることになります。
コードを書く前に、自分が書くコードの処理時間が長すぎないか、あらかじめ時間計算量から見積もっておくことをお勧めいたします。ただし、用途によっては処理時間が長くても問題ない場合もあります。かけられる処理時間は用途によって大きく変わります。ゲームのように 1 フレーム16.6 ms 以内に処理を終わらせなければならない場合もあれば、機械学習のように何日かけてもよい場合もあります。
また、実装内容により処理時間は大幅に変わります。また、 CPU の 1 クロック当たりの命令実行数を正確に見積もることは難しいです。そのため、上記の推定方法は、参考程度にとどめておくことをお勧めいたします。
```

https://github.com/katataku/leetcode/pull/8/changes#r1856437996

```
負の場合、[:k] のところで、予期しないスライスができるか落ちるかで、中途半端にそれらしい値が出てくることになるでしょう。
あまり意味のないものがそれっぽく動き続けるのは、わりとデバッグのときに困ります。

このあたりは、どういう環境に置くか次第なところはあります。
たとえば、ユーザーフェイシングならば、なんらかの結果が見えたほうがいい場合もあるでしょう。夜中に毎日走るパイプラインなどだったらエラーを出して止まってくれたほうが嬉しいでしょう。
常に使い道からこうしたいまでをつなげてください。
```

* step3

優先度つきキューを自作して解決

```
import heapq

class Priority_Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)
    def __bool(self) -> bool:
        return len(self.queue) > 0

    def __getitem__(self, idx):
        return self.queue[idx]

    def push(self, val: int):
        self.queue.append(val)
        idx = len(self.queue) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.queue[parent_idx] <= val:
                break
            self.queue[idx] = self.queue[parent_idx]
            idx = parent_idx
        self.queue[idx] = val
    
    def top(self) -> int:
        if len(self.queue) != 0:
            return self.queue[0]
        return -1
    
    def show(self) -> None:
        print(self.queue)
    
    def pop(self) -> int:
        if len(self.queue) == 0:
            return -1
        top = self.queue[0]
        if len(self.queue) == 1:
            self.queue.pop()
            return top
        last = self.queue.pop()
        idx = 0
        while idx * 2 + 1 < len(self.queue):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            if right_idx < len(self.queue) and self.queue[right_idx] < self.queue[left_idx]:
                child_idx = right_idx
            else:
                child_idx = left_idx
            if last <= self.queue[child_idx]:
                break
            self.queue[idx] = self.queue[child_idx]
            idx = child_idx
        self.queue[idx] = last

        return top

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_largest = k
        self.heap = Priority_Queue()
        
        for num in nums:
            self.heap.push(num)
            if len(self.heap) > self.kth_largest:
                self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if len(self.heap) > self.kth_largest:
            self.heap.pop()
        return self.heap[0]


```