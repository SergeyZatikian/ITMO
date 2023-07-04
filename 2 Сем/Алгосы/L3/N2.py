import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        Этот метод обеспечивает симметричность графика. Другими словами, если существует путь от узла A к B со значением V, должен быть путь от узла B к узлу A со значением V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # Мы будем использовать этот словарь, чтобы сэкономить на посещении каждого узла и обновлять его по мере продвижения по графику 
    shortest_path = {}
 
    # Мы будем использовать этот dict, чтобы сохранить кратчайший известный путь к найденному узлу
    previous_nodes = {}
 
    # Мы будем использовать max_value для инициализации значения "бесконечности" непосещенных узлов   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # Однако мы инициализируем значение начального узла 0  
    shortest_path[start_node] = 0
    
    # Алгоритм выполняется до тех пор, пока мы не посетим все узлы
    while unvisited_nodes:
        # Приведенный ниже блок кода находит узел с наименьшей оценкой
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # Приведенный ниже блок кода извлекает соседей текущего узла и обновляет их расстояния
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # После посещения его соседей мы отмечаем узел как "посещенный"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]


   # Добавить начальный узел вручную
    path.append(start_node)
    
    print("Найден следующий лучший маршрут с ценностью {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

nodes = ['Regent’s Park', 'Goodge Street', 'Bayswater', 'Warren Street', 'Aldgate', 'Farringdon', 'Barbican', 'Russell Square', 'High Street Kensington', 'Old Street',
         'Green Park', 'Baker Street', 'Notting Hill Gate', 'Mansion House', 'Temple', 'Oxford Circus', 'Bond Street', 'Tower Hill', 'Westminster', 'Piccadilly Circus',
         'Charing Cross', 'Holborn', 'Tower Gateway', 'Monument', 'Moorgate', 'Leicester Square', 'St. Paul’s', 'Hyde Park Corner', 'Knightsbridge', 'Angel',
         'Queensway', 'Marble Arch', 'South Kensington', 'Sloane Square', 'Covent Garden', 'Liverpool Street', 'Great Portland Street', 'Bank', 'Chancery Lane',
         'Lancaster Gate', 'Holland Park', 'Cannon Street', 'Fenchurch Street', 'Gloucester Road', 'St. James’s Park', 'Euston Square' , 'Edgware Road', 'Embankment',
         'Blackfriars', 'Tottenham Court Road', 'King’s Cross St. Pancras', 'Paddington', 'Marylebone', 'Kensal Green', 'Queen’s Park', 'Bethnal Green',
         'Cambridge Heath', 'London Fields', 'Willesden Junction', 'Kilburn Park', 'Warwick Avenue', 'Maida Vale', 'Euston', 'Imperial Wharf', 'Clapham Junction',
         'Wapping', 'Denmark Hill', 'Whitechapel', 'Wandsworth Road', 'Rotherhithe', 'Shoreditch High Street', 'Haggerston', 'Hoxton', 'Shepherd’s Bush', 'Shadwell',
         'Canada Water', 'Fulham Broadway', 'West Brompton', 'Parsons Green', 'Putney Bridge', 'East Putney', 'Kensington (Olympia)', 'Aldgate East', 'Bethnal Green',
         'Mile End', 'Dalston Kingsland', 'Hackney Wick', 'Homerton', 'Hackney Central', 'Rectory Road', 'Hackney Downs', 'Dalston Junction', 'Canonbury',
         'Stepney Green', 'Highbury & Islington', 'Clapton', 'Stoke Newington', 'Upper Holloway', 'Gospel Oak', 'Island Gardens', 'Greenwich', 'Deptford Bridge',
         'South Quay', 'Crossharbour', 'Mudchute', 'Heron Quays', 'Elverson Road', 'Cutty Sark for Maritime Greenwich', 'Lewisham', 'Limehouse', 'Manor House',
         'Finsbury Park', 'Arsenal', 'Kentish Town West', 'Holloway Road', 'Caledonian Road', 'Hampstead', 'Belsize Park', 'Chalk Farm', 'Camden Town', 'Archway',
         'Tufnell Park', 'Kentish Town', 'Mornington Crescent', 'Camden Road', 'Caledonian Road & Barnsbury', 'Willesden Green', 'Swiss Cottage', 'Kilburn',
         'West Hampstead', 'Finchley Road', 'St. John’s Wood', 'Turnham Green', 'Stamford Brook', 'Ravenscourt Park' , 'West Kensington', 'Barons Court', 'Earl’s Court',
         'Shepherd’s Bush Market', 'Goldhawk Road', 'Hammersmith', 'Wood Lane', 'White City', 'Finchley Road & Frognal', 'Kensal Rise', 'Brondesbury Park', 'Brondesbury',
         'Kilburn High Road', 'South Hampstead', 'North Acton', 'East Acton', 'Southwark', 'Waterloo', 'London Bridge', 'Bermondsey', 'Vauxhall', 'Lambeth North',
         'Pimlico', 'Stockwell', 'Brixton', 'Elephant & Castle', 'Oval', 'Kennington', 'Borough', 'Stratford', 'Victoria']

print(len(nodes))

init_graph = {}
for node in nodes:
    init_graph[node] = {}

# Red line
init_graph["Holborn"]["Chancery Lane"] = 8
init_graph["Chancery Lane"]["St. Paul’s"] = 14
init_graph["St. Paul’s"]["Bank"] = 9
init_graph["Bank"]["Liverpool Street"] = 10
init_graph["Liverpool Street"]["Bethnal Green"] = 33
init_graph["Bethnal Green"]["Mile End"] = 24
init_graph["Mile End"]["Stratford"] = 43
init_graph["Tottenham Court Road"]["Holborn"] = 10
init_graph["Oxford Circus"]["Tottenham Court Road"] = 9
init_graph["Bond Street"]["Oxford Circus"] = 7
init_graph["Marble Arch"]["Bond Street"] = 7
init_graph["Lancaster Gate"]["Marble Arch"] = 15
init_graph["Queensway"]["Lancaster Gate"] = 10
init_graph["Notting Hill Gate"]["Queensway"] = 8
init_graph["Holland Park"]["Notting Hill Gate"] = 10
init_graph["Shepherd’s Bush"]["Holland Park"] = 11
init_graph["White City"]["Shepherd’s Bush"] = 15
init_graph["East Acton"]["White City"] = 25
init_graph["North Acton"]["East Acton"] = 24

# Blue line
init_graph["Finsbury Park"]["Highbury & Islington"] = 29
init_graph["Highbury & Islington"]["King’s Cross St. Pancras"] = 35
init_graph["King’s Cross St. Pancras"]["Euston"] = 12
init_graph["Euston"]["Warren Street"] = 15
init_graph["Warren Street"]["Oxford Circus"] = 18
init_graph["Oxford Circus"]["Green Park"] = 15
init_graph["Green Park"]["Victoria"] = 19
init_graph["Victoria"]["Pimlico"] = 12
init_graph["Pimlico"]["Vauxhall"] = 18
init_graph["Vauxhall"]["Stockwell"] = 21
init_graph["Stockwell"]["Brixton"] = 16

# City Centre
init_graph["Marylebone"]["Baker Street"] = 6
init_graph["Baker Street"]["Regent’s Park"] = 10
init_graph["Regent’s Park"]["Oxford Circus"] = 15
init_graph["Oxford Circus"]["Piccadilly Circus"] = 12
init_graph["Piccadilly Circus"]["Charing Cross"] = 11
init_graph["Charing Cross"]["Embankment"] = 3
init_graph["Embankment"]["Waterloo"] = 6
init_graph["Edgware Road"]["Baker Street"] = 10
init_graph["Baker Street"]["Great Portland Street"] = 13
init_graph["Great Portland Street"]["Euston Square"] = 10
init_graph["Euston Square"]["King’s Cross St. Pancras"] = 15
init_graph["King’s Cross St. Pancras"]["Farringdon"] = 26
init_graph["Farringdon"]["Barbican"] = 8
init_graph["Barbican"]["Moorgate"] = 10
init_graph["Moorgate"]["Liverpool Street"] = 6
init_graph["Baker Street"]["Bond Street"] = 16
init_graph["Bond Street"]["Green Park"] = 14
init_graph["Green Park"]["Westminster"] = 21
init_graph["Westminster"]["Waterloo"] = 17
init_graph["Warren Street"]["Goodge Street"] = 7
init_graph["Goodge Street"]["Tottenham Court Road"] = 7
init_graph["Tottenham Court Road"]["Leicester Square"] = 8
init_graph["Leicester Square"]["Charing Cross"] = 7
init_graph["King’s Cross St. Pancras"]["Russell Square"] = 14
init_graph["Russell Square"]["Holborn"] = 9
init_graph["Holborn"]["Covent Garden"] = 8
init_graph["Covent Garden"]["Leicester Square"] = 4
init_graph["Leicester Square"]["Piccadilly Circus"] = 6
init_graph["Piccadilly Circus"]["Green Park"] = 8
init_graph["Green Park"]["Hyde Park Corner"] = 12
init_graph["Hyde Park Corner"]["Knightsbridge"] = 7
init_graph["Knightsbridge"]["South Kensington"] = 17
init_graph["South Kensington"]["Gloucester Road"] = 8
init_graph["South Kensington"]["Sloane Square"] = 17
init_graph["Sloane Square"]["Victoria"] = 13
init_graph["Victoria"]["St. James’s Park"] = 11
init_graph["St. James’s Park"]["Westminster"] = 11
init_graph["Westminster"]["Embankment"] = 10
init_graph["Embankment"]["Temple"] = 9
init_graph["Temple"]["Blackfriars"] = 10
init_graph["Blackfriars"]["Mansion House"] = 10
init_graph["Mansion House"]["Cannon Street"] = 4
init_graph["Cannon Street"]["Bank"] = 5
init_graph["King’s Cross St. Pancras"]["Angel"] = 16
init_graph["Angel"]["Old Street"] = 20
init_graph["Old Street"]["Moorgate"] = 9
init_graph["Moorgate"]["Bank"] = 9
init_graph["Bank"]["London Bridge"] = 6

graph = Graph(nodes, init_graph)

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Marylebone")

print_result(previous_nodes, shortest_path, start_node="Marylebone", target_node="London Bridge")