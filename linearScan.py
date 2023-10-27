def linearScan(graph, registers, fitness):
    freeRegisters = [True for i in range(registers)]
    liveRanges, totalSpill = getLiveRanges(graph)
    result = {
        "NodesNumber" : len(liveRanges),
        "validColors" : len(liveRanges),
        "spillCost" : 0
    }
    actives =  []
    for node_name in liveRanges:
        node = liveRanges[node_name]
        for node_name2 in actives:
            node2 = liveRanges[node_name2]
            if node2["end"] <= node["begin"]:
                actives.remove(node_name2)
                if node["reg"] != -1:
                    freeRegisters[node["reg"] - 1] = True
        if len(actives) == registers:
            node["reg"] == -1
            result["validColors"] -= 1
            result["spillCost"] += node["spillCost"]
        else:
            for i in range(registers):
                if freeRegisters[i]:
                    freeRegisters[i] = False
                    node["reg"] = i + 1
            actives.append(node_name)
    if fitness:
        result["fitness"] = 1 - result["spillCost"]/totalSpill
    return result


def getLiveRanges(graph):
    liveRanges = {}
    totalSpill = 0
    nodes = graph["nodes"]
    for node_name in nodes:
        node = nodes[node_name]
        liveRange = {"reg" : 0}
        liveRange["begin"] = node["uses"][0]
        liveRange["end"] = node["uses"][-1]
        liveRange["spillCost"] = spillCost(node)
        totalSpill += liveRange["spillCost"]
        liveRanges[node_name] = liveRange
    return dict(sorted(liveRanges.items(), key=lambda item: item[1]['begin'])), totalSpill


def spillCost(node):
    spillCost = 0
    for i in node["uses deepness"]:
        spillCost += 10**i
    return spillCost


