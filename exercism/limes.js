const limes = [
    'small',
    'large',
    'large',
    'medium',
    'small',
    'large',
    'large',
    'medium',
];
function limesToCut(wedgesNeeded, limesList) {
    let cutWedges = 0;
    let cutLimes = 0;
    
    
    do {
        let currentLime = limesList.shift();
        console.log(currentLime);
        switch (currentLime) {
            case "small":
                cutWedges += 6;
                break;
            case "medium":
                cutWedges += 8;
                break;
            case "large":
                cutWedges += 10;
                break;
            };
        console.log("cutWedges : ", cutWedges);
        cutLimes ++;
    } while (cutWedges < wedgesNeeded && limesList.length !==0);

    console.log("Limes cut : ", cutLimes);
    return cutLimes
}

function timeToMixJuice(name) {
    switch (name) {
      case "Pure Strawberry Joy":
        return 0.5;
      case "Energizer":
        return 1.5;
      case "Green Garden":
        return 1.5;
      case "Tropical Island":
        return 3;
      case "All or Nothing":
        return 5;
      default:
        return 2.5;
    }
}

const ordersLeft = ['Energizer', 'All or Nothing', 'Green Garden']

function remainingOrders(timeLeft, orders) {
    
    while (timeLeft > 0) {
        timeLeft -= timeToMixJuice(orders.shift())
    }  
    return orders
}

