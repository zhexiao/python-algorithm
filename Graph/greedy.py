"""
贪心算法：
贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。
也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。

算法效率是：O(n^2)
"""
# 需要覆盖的地点
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 每个电台覆盖的地点
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 选择最少的电台可以覆盖所有的地点
final_stations = set()

# 算法开始，每次找到能够覆盖最多地点的station
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # 求并集，拿到这个station能够覆盖的地点
        coverd = states_needed & states_for_station
        if len(coverd) > len(states_covered):
            best_station = station
            states_covered = coverd

    final_stations.add(best_station)
    # 求差集，去掉已经匹配的地点
    states_needed -= states_covered

print(final_stations)