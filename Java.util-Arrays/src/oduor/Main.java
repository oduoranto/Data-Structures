package oduor;

import java.util.Arrays;
import java.util.Random;

public class Main {

    public static  void main(String[] args){

        int[] results = getRandom(10);

        System.out.println(Arrays.toString(results));

         Arrays.sort(results);
        System.out.println(Arrays.toString(results));

        int[] firstArray = new int[10];
        Arrays.fill(firstArray, 89);
        System.out.println(Arrays.toString(firstArray));


        String [] names = {"Anto", "Davis","Johnny", "Libra"};

        if(Arrays.binarySearch(names, "Anto") >= 0){
            System.out.println("Found on the list");
        }else{
            System.out.println("Not found on the ist");
        }



    }
    private static int[] getRandom(int len){

        Random random = new Random();
        int[] getNum = new int[len];

        for(int i = 0; i < len; i++){

            getNum[i] = random.nextInt();
        }
        return getNum;
    }
}
