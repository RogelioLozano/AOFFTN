import numpy as np
import scipy.spatial as sp

def hopkins_stat(X,p,trials=50):

    """
    Computes the Hopkins statistic (A measure of clustering tendency, i.e., a measure to assess if a data set
    has cluster structure or not.)

    Parameters:
    -----------
    X: np.array [n_samples_a, n_features]
        Feature array
    p: integer 
        Number of random datapoints and sampled datapoints to be generated.
    trials: integer
        Number of times the hopkins statistic will be computed.

    Returns:
    --------
    np.array of size trials of computed hopkins statistics.  
    """

    Hopkins_list = []
    for _ in range(trials):

        generated = np.random.uniform(size=(p,2))
        us = np.zeros(p)
        for i,point in enumerate(generated):
            feature_matrix = np.concatenate([point.reshape(-1,2),X])
            dist = sp.distance.squareform(sp.distance.pdist(feature_matrix))
            nearest_neighbor_index = np.argmin(dist[0][1:]) + 1
            nearest_neighbor_distance = dist[0][nearest_neighbor_index]
            us[i] = nearest_neighbor_distance

        sample = np.random.choice(X.shape[0],p,replace=False)
        ws = np.zeros(p)
        for i,index in enumerate(sample):
            to_insert = X[index]
            newX=np.delete(X,index,axis=0)
            newX = np.insert(newX,0,to_insert,axis=0)
            dist = sp.distance.squareform(sp.distance.pdist(newX))
            nearest_neighbor_index = np.argmin(dist[0][1:]) + 1
            nearest_neighbor_distance = dist[0][nearest_neighbor_index]
            ws[i] = nearest_neighbor_distance    

        Hopkins = np.sum(ws) / ( np.sum(us)+np.sum(ws) )

        Hopkins_list.append(Hopkins)

    return np.array(Hopkins_list)
