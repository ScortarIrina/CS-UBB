//
// Created by irina on 25.05.2022.
//

#ifndef GA_LAB5_EDGE_H
#define GA_LAB5_EDGE_H

class Edge {
public:
    int srcVertex;
    int destVertex;

    Edge(int srcVertex, int destVertex);
    bool operator == (const Edge& newEdge) const;
    bool operator != (const Edge& newEdge) const;
};


#endif //GA_LAB5_EDGE_H
