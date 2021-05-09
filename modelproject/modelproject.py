def simulate_basic(k,alpha,delta,s,n,g,K,T,D):
    """
    Args:
    k      (int)  : initial value for physical capital per worker
    alpha  (float): return on physical capital
    delta  (float): depreciation rate on capital
    s      (float): savings/investments
    n      (float): increase in labour
    g             : growth
    K      (int)  : totalfactorproductivity
    T      (int)  : periods to simulate through
    D             : climate change
    
    Returns:
    A plot showing how capital per worker accumulates over time"""
    
    #First we make a list for our future values to be in
    k_path = [k]
    
    #Then we make which will contain the values for the 45-degree-line
    Degreeline = [0]
    
    #We generate the 45-degree-line for the basic Solow model
    for t in range(1,T):
        line = (n+g+delta)*t
        Degreeline.append(line)
        
    #We generate the Solow movement
    for t in range(1,T):
        k_plus = s*(1-D)*K*t**alpha
        k_path.append(k_plus)
    
    #Plotting the stuff
    plt.figure(figsize=(7,7))
    plt.plot(k_path[:T], label='$s(1-D)k_t^{\u03B1}$', color = 'red')
    plt.plot(Degreeline[:T], label = '$k_t(n+\delta+g)$', color = 'blue')
    plt.xlim(0,T)
    plt.ylim(0,Degreeline[-1])
    plt.xlabel('$k_t$')
    plt.grid(True)
    plt.legend()
    
    return plt.show()