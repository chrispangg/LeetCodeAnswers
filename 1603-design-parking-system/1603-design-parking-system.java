class ParkingSystem {
    
    int[] spaceAvailable;

    public ParkingSystem(int big, int medium, int small) {
        
        spaceAvailable = new int[4];
        spaceAvailable[0] = 0;
        spaceAvailable[1] = big;
        spaceAvailable[2] = medium;
        spaceAvailable[3] = small;
        
    }
    
    public boolean addCar(int carType) {
        boolean available = false;
        
        for(int i = 0; i < spaceAvailable.length; i++){
            if(spaceAvailable[i] !=0 & i == carType){
                spaceAvailable[i] -=1;
                available = true;
            }
        }
        return available;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */