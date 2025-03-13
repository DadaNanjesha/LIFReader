import networkx as nx

class LIFGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        """
        Add a node to the graph with all its properties.
        """
        self.graph.add_node(
            node.node_id,
            pos=(node.node_position["x"], node.node_position["y"]), 
            node_id=node.node_id, 
            node_name=node.node_name,  
            node_description=node.node_description,  
            map_id=node.map_id,
            node_type=node.node_type,  # Node type (e.g., "parking", "drop", "station")
            vehicle_type_node_properties=node.vehicle_type_node_properties, 
            actions=node.actions  # List of actions
        )

    def add_edge(self, edge):
        """
        Add an edge to the graph with all its properties.
        """
        self.graph.add_edge(
            edge.start_node_id,
            edge.end_node_id,
            edge_id=edge.edge_id, 
            edge_name=edge.edge_name,  
            edge_description=edge.edge_description,
            vehicle_type_edge_properties=edge.vehicle_type_edge_properties  
        )

    def add_station(self, station):
        """
        Add a station to the graph with all its properties.
        """
        for node_id in station.interaction_node_ids:
            if node_id in self.graph:
                self.graph.nodes[node_id].update({
                    "station_id": station.station_id,  
                    "station_name": station.station_name,  
                    "station_description": station.station_description,  
                    "station_height": station.station_height,  
                    "station_position": station.station_position,  
                    "station_type": station.station_type
                })

    def get_graph(self):
        """
        Return the constructed graph with all properties.
        """
        return self.graph