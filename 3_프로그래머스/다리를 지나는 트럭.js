// https://programmers.co.kr/learn/courses/30/lessons/42583


function solution(bridge_length, weight, truck_weights) {
    let bridge = []
    let time = -1;
    let current = -1;

    for (let i = 0; i < bridge_length-1; i++)
        bridge.push(0)

    current = truck_weights[0];
    bridge.push(truck_weights[0]);
    truck_weights.shift()
    time = 1;

    while (current > 0) {
        current -= bridge.shift();

        if (truck_weights.length != 0)
        {
            if (truck_weights[0] + current <= weight) {
                current += truck_weights[0];
                bridge.push(truck_weights[0])
                truck_weights.shift();
            }
            else 
                bridge.push(0);
        }
        time++;
    }

    return time;
}