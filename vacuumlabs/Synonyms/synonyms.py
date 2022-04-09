import networkx as nx

def get_inputs(file):
    synonyms_list = []
    queries_list = []

    N = int(file.readline())
    for _ in range(N):
        synonym_one, synonym_two = file.readline().split(sep=' ')
        synonyms_list.append((synonym_one.casefold(), synonym_two.rstrip().casefold()))
    
    Q = int(file.readline())
    for _ in range(Q):
        query_one, query_two = file.readline().split(sep=' ')
        queries_list.append((query_one.casefold(), query_two.rstrip().casefold()))
    return synonyms_list, queries_list

def synonyms(synomyms, queries):
    graph = nx.Graph()
    graph.add_edges_from(synomyms)

    output = []
    for query in queries:
        if query[0] == query[1]:
            output.append('synonyms')
            continue

        try:
            if nx.has_path(graph, query[0], query[1]):
                output.append('synonyms')
            else:
                output.append('different')
        except nx.NodeNotFound:
            output.append('different')
    
    return output


if __name__ == '__main__':
    output = []

    with open('test.in') as file:
        T = int(file.readline())
        for i in range(T):
            synonyms_list, queries_list = get_inputs(file)
            testcase_output = synonyms(synonyms_list, queries_list)
            output += testcase_output

    with open('test.out', 'a') as file:
        for item in output:
            file.write("%s\n" % item)
