class range_map:
    def __init__(self, dest, source, length):
        self.start = source
        self.end = source + length
        self.offset = dest - source
        assert self.start < self.end
    
    def __call__(self, value):
        if self.start <= value and value < self.end:
            return value + self.offset
        return value

    def __repr__(self):
        return "[{}, {}, {}]".format(self.start, self.end, self.offset)

    def from_line(line):
        dst_str, src_str, range_str = line.split(" ")
        return range_map(int(dst_str), int(src_str), int(range_str))

def are_ranges_disjoint(range_list):
    for i in range(0, len(range_list)):
        start_i = range_list[i].start
        end_i = range_list[i].end - 1
        for k in range(i + 1, len(range_list)):
            start_k = range_list[k].start
            end_k = range_list[k].end - 1
            if not ((end_i < start_k) or (end_k < start_i)):
                print(range_list[i])
                print(range_list[k])
                return False
    return True

class category_map:
    def __init__(self, range_maps : list):
        self.range_maps = range_maps
        assert are_ranges_disjoint(self.range_maps)
    
    def __str__(self):
        return str(self.range_maps)
    
    def __call__(self, value):
        for m in self.range_maps:
            mapped_value = m(value)
            if mapped_value != value:
                return mapped_value
        return value
        
with open("input.txt") as f:
    seeds = []
    category_maps = []
    range_maps = []
    for line in f:
        line = line.strip()
        if line.find("seeds:") > -1:
            seeds = map(int, line[line.index(":") + 2:].split(" "))
            continue
        if len(line) <= 0:
            # End of a category
            if len(range_maps) > 0:
                category_maps.append(category_map(range_maps))
            continue
        if line.find("-to-") > -1:
            # A new category starts
            range_maps = []
            continue
        range_maps.append(range_map.from_line(line))
    
    seeds = list(seeds)
    results = seeds
    for category in category_maps:
        results = list(map(category, results))
    
    print("Part 1: ", min(results))